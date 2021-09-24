from common.utils.attack_utils import ScanStatus
from monkey_island.cc.services.attack.technique_reports.__init__ import (
    AttackTechnique,
    disabled_msg,
)

FAKE_CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE = {
    "T0000": {
        "Definition Type 1": ["Config Option 1", "Config Option 2"],
        "Definition Type 2": ["Config Option 5", "Config Option 6"],
    },
    "T0001": {
        "Definition Type 1": ["Config Option 1"],
        "Definition Type 2": ["Config Option 5"],
    },
}


class FakeAttackTechnique_TwoRelevantSystems(AttackTechnique):
    tech_id = "T0001"
    relevant_systems = ["System 1", "System 2"]
    unscanned_msg = "UNSCANNED"
    scanned_msg = "SCANNED"
    used_msg = "USED"

    def get_report_data():
        pass


EXPECTED_UNSCANNED_MSG_TWO_RELEVANT_SYSTEMS = (
    "UNSCANNED due to one of the following reasons:\n"
    "- The following configuration options were disabled:<br/>"
    "- Definition Type 1 — Config Option 1<br/>"
    "- Definition Type 2 — Config Option 5<br/>"
)


EXPECTED_SCANNED_MSG_TWO_RELEVANT_SYSTEMS = "SCANNED"


EXPECTED_USED_MSG_TWO_RELEVANT_SYSTEMS = "USED"


class FakeAttackTechnique_OneRelevantSystem(AttackTechnique):
    tech_id = "T0001"
    relevant_systems = ["System 1"]
    unscanned_msg = "UNSCANNED"
    scanned_msg = "SCANNED"
    used_msg = "USED"

    def get_report_data():
        pass


EXPECTED_UNSCANNED_MSG_ONE_RELEVANT_SYSTEM = (
    "UNSCANNED due to one of the following reasons:\n"
    "- The Monkey did not run on any System 1 systems.\n"
    "- The following configuration options were disabled:<br/>"
    "- Definition Type 1 — Config Option 1<br/>"
    "- Definition Type 2 — Config Option 5<br/>"
)


EXPECTED_SCANNED_MSG_ONE_RELEVANT_SYSTEM = "SCANNED"


EXPECTED_USED_MSG_ONE_RELEVANT_SYSTEM = "USED"


def test_get_message_by_status_disabled_two_relevant_systems(monkeypatch):
    monkeypatch.setattr(
        (
            "monkey_island.cc.services.attack.technique_reports."
            "__init__.CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE"
        ),
        FAKE_CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE,
    )
    technique_msg = FakeAttackTechnique_TwoRelevantSystems.get_message_by_status(
        ScanStatus.DISABLED.value
    )
    assert technique_msg == disabled_msg


def test_get_message_by_status_unscanned_two_relevant_systems(monkeypatch):
    monkeypatch.setattr(
        (
            "monkey_island.cc.services.attack.technique_reports."
            "__init__.CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE"
        ),
        FAKE_CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE,
    )
    technique_msg = FakeAttackTechnique_TwoRelevantSystems.get_message_by_status(
        ScanStatus.UNSCANNED.value
    )
    assert technique_msg == EXPECTED_UNSCANNED_MSG_TWO_RELEVANT_SYSTEMS


def test_get_message_by_status_scanned_two_relevant_systems(monkeypatch):
    monkeypatch.setattr(
        (
            "monkey_island.cc.services.attack.technique_reports."
            "__init__.CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE"
        ),
        FAKE_CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE,
    )
    technique_msg = FakeAttackTechnique_TwoRelevantSystems.get_message_by_status(
        ScanStatus.SCANNED.value
    )
    assert technique_msg == EXPECTED_SCANNED_MSG_TWO_RELEVANT_SYSTEMS


def test_get_message_by_status_used_two_relevant_systems(monkeypatch):
    monkeypatch.setattr(
        (
            "monkey_island.cc.services.attack.technique_reports."
            "__init__.CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE"
        ),
        FAKE_CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE,
    )
    technique_msg = FakeAttackTechnique_TwoRelevantSystems.get_message_by_status(
        ScanStatus.USED.value
    )
    assert technique_msg == EXPECTED_USED_MSG_TWO_RELEVANT_SYSTEMS


###


def test_get_message_by_status_disabled_one_relevant_system(monkeypatch):
    monkeypatch.setattr(
        (
            "monkey_island.cc.services.attack.technique_reports."
            "__init__.CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE"
        ),
        FAKE_CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE,
    )
    technique_msg = FakeAttackTechnique_OneRelevantSystem.get_message_by_status(
        ScanStatus.DISABLED.value
    )
    assert technique_msg == disabled_msg


def test_get_message_by_status_unscanned_one_relevant_system(monkeypatch):
    monkeypatch.setattr(
        (
            "monkey_island.cc.services.attack.technique_reports."
            "__init__.CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE"
        ),
        FAKE_CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE,
    )
    technique_msg = FakeAttackTechnique_OneRelevantSystem.get_message_by_status(
        ScanStatus.UNSCANNED.value
    )
    assert technique_msg == EXPECTED_UNSCANNED_MSG_ONE_RELEVANT_SYSTEM


def test_get_message_by_status_scanned_one_relevant_system(monkeypatch):
    monkeypatch.setattr(
        (
            "monkey_island.cc.services.attack.technique_reports."
            "__init__.CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE"
        ),
        FAKE_CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE,
    )
    technique_msg = FakeAttackTechnique_OneRelevantSystem.get_message_by_status(
        ScanStatus.SCANNED.value
    )
    assert technique_msg == EXPECTED_SCANNED_MSG_ONE_RELEVANT_SYSTEM


def test_get_message_by_status_used_one_relevant_system(monkeypatch):
    monkeypatch.setattr(
        (
            "monkey_island.cc.services.attack.technique_reports."
            "__init__.CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE"
        ),
        FAKE_CONFIG_SCHEMA_PER_ATTACK_TECHNIQUE,
    )
    technique_msg = FakeAttackTechnique_OneRelevantSystem.get_message_by_status(
        ScanStatus.USED.value
    )
    assert technique_msg == EXPECTED_USED_MSG_ONE_RELEVANT_SYSTEM
