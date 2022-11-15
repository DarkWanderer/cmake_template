import json
import argparse


def get_base_configure_preset(generator: str):
    return {
        "name": generator.lower() + "-base",
        "hidden": True,
        "generator": "Unix Makefiles" if generator == 'Make' else generator,
        "binaryDir": "${sourceDir}/out/build/" + generator.lower() + "/${presetName}",
        "installDir": "${sourceDir}/out/install/${presetName}"
    }


def get_os_base_configure_preset(os: str, inherits: str):
    result = {
        "name": os.lower() + "-base",
        "hidden": True,
        "inherits": inherits,
        "condition": {
            "type": "equals",
            "lhs": "${hostSystemName}",
            "rhs": "Darwin" if os == "macOS" else os
        }
    }
    if os == 'Windows':
        result["cacheVariables"] = {
            "CMAKE_C_COMPILER": "cl.exe",
            "CMAKE_CXX_COMPILER": "cl.exe"
        }
    else:
        result["cacheVariables"] = {
            "CMAKE_C_COMPILER": "gcc",
            "CMAKE_CXX_COMPILER": "g++"
        }
        result["vendor"] = {
            "microsoft.com/VisualStudioSettings/CMake/1.0": {"hostOS": [os]},
            "microsoft.com/VisualStudioRemoteSettings/CMake/1.0": {"sourceDir": "$env{HOME}/.vs/$ms{projectDirName}"}
        }
    return result


def get_os_preset(os: str, inherits: str, arch: str, conf: str):
    result = {
        "name": os.lower() + "-" + arch + "-" + conf.lower(),
        "inherits": inherits,
        "displayName": arch + " " + conf,
        "architecture": {"value": arch, "strategy": "external"},
        "cacheVariables": {
            "CMAKE_BUILD_TYPE": "Debug" if conf == "ASan" else conf,
            "ASAN_ENABLED": conf == "ASan"
        }
    }
    return result


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog='generate-cmakepresets',
        description='Generates CMakePresets.json file with custom parameters'
    )
    parser.add_argument('--file', default='CMakePresets.json')
    parser.add_argument(
        '--generator',
        default='Ninja',
        choices=[
            'Ninja',
            'Make'])
    parser.add_argument('--macos', action='store_true')
    args = parser.parse_args()
    print(args)

    configure_presets = []
    build_presets = []
    test_presets = []

    base_configure_preset = get_base_configure_preset(args.generator)
    base_build_preset = {
        'name': 'build-base',
        'hidden': True,
        'jobs': 1,
        'cleanFirst': False
    }
    base_test_preset = {
        "name": "test-base",
        "description": "Basic shared test settings",
        "hidden": True,
        "execution": {
            "noTestsAction": "error",
            "stopOnFailure": False
        },
        "output": {
            "outputOnFailure": True
        }
    }
    configure_presets.append(base_configure_preset)
    build_presets.append(base_build_preset)
    test_presets.append(base_test_preset)

    os_names = [
        "Linux",
        "Windows",
        "macOS"] if args.macos else [
        "Linux",
        "Windows"]

    for os in os_names:
        os_base_configure_preset = get_os_base_configure_preset(
            os, base_configure_preset["name"])
        configure_presets.append(os_base_configure_preset)
        for conf in ["Debug", "Release", "ASan"]:
            configure_presets.append(
                get_os_preset(
                    os,
                    os_base_configure_preset["name"],
                    "x64",
                    conf))
            if os == "Windows":
                configure_presets.append(
                    get_os_preset(
                        os,
                        os_base_configure_preset["name"],
                        "x86",
                        conf))

    for conf_preset in configure_presets:
        if conf_preset.get('hidden', False) == True:
            continue
        build_presets.append({
            "name": conf_preset["name"],
            "inherits": base_build_preset["name"],
            "displayName": conf_preset["displayName"],
            "configurePreset": conf_preset["name"],
        })
        test_presets.append({
            "name": conf_preset["name"],
            "inherits": base_test_preset["name"],
            "displayName": conf_preset["displayName"],
            "configurePreset": conf_preset["name"],
        })

    root_presets = {
        "version": 3,
        "configurePresets": configure_presets,
        "buildPresets": build_presets,
        "testPresets": test_presets
    }

    with open(args.file, 'w') as f:
        json.dump(root_presets, f, indent=2)
