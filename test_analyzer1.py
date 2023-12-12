from invoke_analyzer import collect_uninvoked_methods

test_input_path = "./src"
input_one ="./myapp/"
input_two ="./buildozer/"
input_three ="./Sudoku-Solver"
input_four ="./contrib"

def test_methods_uninvoked():
    expected = {
                "C": set(),
                "A": {"__init__", "func1"},
                "B": {"f1", "f2"}
      }

    result = collect_uninvoked_methods(test_input_path)
    assert expected == result

def test_one():
    expected = {'Users': {'__str__'}, 'MyappConfig': set(), 'login': set(), 'signup': set(), 'reset_form': set(), 'Migration': set()}
    result = collect_uninvoked_methods(input_one)
    assert expected == result
    print(result)

def test_two():
    expected = {'SpecParser': {'__init__', 'read_dict', 'read_file', 'read', 'read_string', 'optionxform', 'getlistvalues', 'getbooldefault', 'apply_profile'}, 'JsonStore': {'__init__', '__getitem__', '__delitem__', 'get', 'keys', '__setitem__', '__contains__'}, '_StreamReader': {'__init__', 'read', '_fill_queue'}, 'Buildozer': {'applibs_dir', 'prepare_for_build', 'global_buildozer_dir', 'build', 'cmd_help', 'cmd_version', 'get_version', 'app_dir', 'cmd_appclean', 'cmd_setdefault', 'user_build_dir', 'cmd_serve', 'root_dir', 'clean_platform', '__init__', 'cmd_distclean', 'namify', 'global_cache_dir', 'global_packages_dir', 'platform_dir', 'buildozer_dir', 'package_full_name', 'global_platform_dir', 'cmd_init', 'bin_dir'}, 'Logger': {'log_env', 'set_level', 'debug', 'error', 'info'}, 'BuildozerException': set(), 'BuildozerCommandException': set(), 'Target': {'cmd_deploy', '__init__', 'check_requirements', 'run_commands', 'get_custom_commands', 'cmd_update', 'cmd_debug', 'cmd_run', 'get_available_packages', 'cmd_serve', 'install_or_update_repo', 'cmd_release', 'cmd_clean', 'compile_platform', 'install_platform'}, 'TargetIos': {'cmd_deploy', '__init__', 'check_requirements', 'cmd_xcode', 'cmd_run', 'compile_platform', 'build_package', 'check_configuration_tokens', 'code_signing_development_team', 'cmd_list_identities', 'code_signing_allowed', 'install_platform'}, 'TargetAndroid': {'cmd_deploy', '_find_latest_package', 'build_package', 'p4a_dir', 'android_sdk_dir', 'cmd_run', 'android_api', 'cmd_release', 'apache_ant_dir', '__init__', 'cmd_p4a', 'cmd_debug', 'archs_snake', 'cmd_adb', 'get_available_packages', 'sdkmanager_path', 'android_ndk_version', 'cmd_clean', 'serials', 'cmd_logcat', 'android_ndk_dir', 'android_minapi', 'p4a_recommended_android_ndk', 'compile_platform'}, 'TargetOSX': {'run_commands', 'check_requirements', 'get_available_packages', 'build_package', 'install_platform'}, 'InvalidVersion': set(), '_BaseVersion': {'__gt__', '__lt__', '__ne__', '__eq__', '__hash__', '__le__', '__ge__'}, 'LegacyVersion': {'__init__', '__repr__', 'is_prerelease', 'is_postrelease', 'base_version', 'local', 'public', '__str__'}, 'Version': {'__init__', '__repr__', 'is_prerelease', 'is_postrelease', 'base_version', 'local', 'public', '__str__'}, 'Infinity': {'__repr__', '__gt__', '__lt__', '__ne__', '__eq__', '__neg__', '__hash__', '__le__', '__ge__'}, 'NegativeInfinity': {'__repr__', '__gt__', '__lt__', '__ne__', '__eq__', '__neg__', '__hash__', '__le__', '__ge__'}, 'BuildozerRemote': {'run_command', 'writeall'}}
    result = collect_uninvoked_methods(input_two)
    assert  expected == result
    print(result)


def test_three():
    expected = {'Board': {'__init__', 'deselect', 'hint'}, 'Tile': {'__init__', 'draw', 'clicked', 'display'}}
    result = collect_uninvoked_methods(input_three)
    assert expected == result
    print(result)

def test_four():
    expected = {'_TqdmLoggingHandler': {'__init__', 'emit'}, 'TelegramIO': {'delete', 'message_id', '__init__', 'write'}, 'tqdm_telegram': {'clear', '__init__', 'display', 'close'}, 'DiscordIO': {'__init__', 'write'}, 'tqdm_discord': {'clear', '__init__', 'display'}, 'DummyTqdmFile': {'__del__', '__init__', 'write'}, 'SlackIO': {'__init__', 'write'}, 'tqdm_slack': {'clear', '__init__', 'display'}, 'MonoWorker': {'submit', '__init__'}}

    result = collect_uninvoked_methods(input_four)
    assert expected == result
    print(result)
