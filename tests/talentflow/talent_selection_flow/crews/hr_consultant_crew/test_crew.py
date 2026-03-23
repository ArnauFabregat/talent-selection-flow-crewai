import pytest

from talentflow.talent_selection_flow.crews.hr_consultant_crew.crew import HRConsultingCrew


def test_init_with_default_parameters():
    """
    Test that HRConsultingCrew initializes with default parameters.
    """
    # Arrange
    # Act
    crew = HRConsultingCrew()

    # Assert
    # Verify attributes are set correctly
    assert crew._verbose is False


def test_init_with_verbose_enabled():
    """
    Test that HRConsultingCrew initializes with verbose=True.
    """
    # Arrange
    # Act
    crew = HRConsultingCrew(verbose=True)

    # Assert
    # Verify attributes are set correctly
    assert crew._verbose is True


def test_init_with_invalid_verbose_type():
    """
    Test that HRConsultingCrew handles invalid verbose type.
    """
    # Arrange
    # Act
    crew = HRConsultingCrew(verbose=1)  # Non-boolean value

    # Assert
    # Verify attributes are set correctly (accepts any value)
    assert crew._verbose == 1


def test_init_with_none_verbose():
    """
    Test that HRConsultingCrew accepts None for verbose parameter.
    """
    # Arrange
    # Act
    crew = HRConsultingCrew(verbose=None)

    # Assert
    # Verify attributes are set correctly
    assert crew._verbose is None


def test_consultant_agent_with_missing_config():
    """
    Test that consultant_agent handles missing config.
    """
    # Arrange
    crew = HRConsultingCrew()
    crew.agents_config = {}  # Empty config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.consultant_agent()


def test_consulting_task_with_missing_tasks_config():
    """
    Test that consulting_task handles missing tasks_config gracefully.
    """
    # Arrange
    crew = HRConsultingCrew()
    crew.agents_config = {"consultant_agent": {"name": "HR Consultant"}}
    crew.tasks_config = {}  # Empty tasks_config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.consulting_task()


def test_consulting_task_with_missing_agents_config():
    """
    Test that consulting_task handles missing agents_config gracefully.
    """
    # Arrange
    crew = HRConsultingCrew()
    crew.agents_config = {}
    crew.tasks_config = {
        "consulting_task": {"description": "Analyze technical data", "expected_output": "HR recommendations"}
    }

    # Act & Assert
    with pytest.raises(KeyError):
        crew.consulting_task()


def test_crew_with_missing_config():
    """
    Test that crew handles missing configuration gracefully.
    """
    # Arrange
    crew = HRConsultingCrew()
    crew.agents_config = {}
    crew.tasks_config = {}

    # Act & Assert
    with pytest.raises(KeyError):
        crew.crew()
