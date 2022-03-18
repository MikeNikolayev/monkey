import hashlib
import os
import sys
import uuid
from abc import ABCMeta
from itertools import product

GUID = str(uuid.getnode())

EXTERNAL_CONFIG_FILE = os.path.join(os.path.abspath(os.path.dirname(sys.argv[0])), "monkey.bin")

SENSITIVE_FIELDS = [
    "exploit_password_list",
    "exploit_user_list",
    "exploit_ssh_keys",
    "aws_secret_access_key",
    "aws_session_token",
]
LOCAL_CONFIG_VARS = ["name", "id", "current_server", "max_depth"]
HIDDEN_FIELD_REPLACEMENT_CONTENT = "hidden"


class Configuration(object):
    def from_kv(self, formatted_data):
        unknown_items = []
        for key, value in list(formatted_data.items()):
            if key.startswith("_"):
                continue
            if key in LOCAL_CONFIG_VARS:
                continue
            if hasattr(self, key):
                setattr(self, key, value)
            else:
                unknown_items.append(key)
        if not self.max_depth:
            self.max_depth = self.depth
        return unknown_items

    @staticmethod
    def hide_sensitive_info(config_dict):
        for field in SENSITIVE_FIELDS:
            config_dict[field] = HIDDEN_FIELD_REPLACEMENT_CONTENT
        return config_dict

    def as_dict(self):
        result = {}
        for key in dir(Configuration):
            if key.startswith("_"):
                continue
            try:
                value = getattr(self, key)
            except AttributeError:
                continue

            val_type = type(value)

            if callable(value):
                continue

            if val_type in (type, ABCMeta):
                value = value.__name__
            elif val_type is tuple or val_type is list:
                if len(value) != 0 and type(value[0]) in (type, ABCMeta):
                    value = val_type([x.__name__ for x in value])

            result[key] = value

        return result

    ###########################
    # dropper config
    ###########################

    dropper_set_date = True
    dropper_date_reference_path_windows = r"%windir%\system32\kernel32.dll"
    dropper_date_reference_path_linux = "/bin/sh"
    dropper_target_path_win_64 = r"C:\Windows\temp\monkey64.exe"
    dropper_target_path_linux = "/tmp/monkey"

    ###########################
    # monkey config
    ###########################
    # sets whether or not the monkey is alive. if false will stop scanning and exploiting
    should_stop = False

    # depth of propagation
    depth = 2
    max_depth = None
    current_server = ""

    # Configuration servers to try to connect to, in this order.
    command_servers = ["192.0.2.0:5000"]

    keep_tunnel_open_time = 60

    def get_exploit_user_password_pairs(self):
        """
        Returns all combinations of the configurations users and passwords
        :return:
        """
        return product(self.exploit_user_list, self.exploit_password_list)

    @staticmethod
    def hash_sensitive_data(sensitive_data):
        """
        Hash sensitive data (e.g. passwords). Used so the log won't contain sensitive data
        plain-text, as the log is
        saved on client machines plain-text.

        :param sensitive_data: the data to hash.
        :return: the hashed data.
        """
        password_hashed = hashlib.sha512(sensitive_data.encode()).hexdigest()
        return password_hashed

    exploit_user_list = ["Administrator", "root", "user"]
    exploit_password_list = ["Password1!", "1234", "password", "12345678"]
    exploit_lm_hash_list = []
    exploit_ntlm_hash_list = []

    # smb/wmi exploiter
    smb_download_timeout = 30  # timeout in seconds

    ###########################
    # post breach actions
    ###########################
    post_breach_actions = []
    custom_PBA_linux_cmd = ""
    custom_PBA_windows_cmd = ""
    PBA_linux_filename = None
    PBA_windows_filename = None

    ###########################
    # testing configuration
    ###########################
    export_monkey_telems = False


WormConfiguration = Configuration()
