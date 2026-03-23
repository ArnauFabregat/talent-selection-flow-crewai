import pytest

from talentflow.talent_selection_flow.crews.classification_crew.crew import ClassificationCrew


def test_init_with_custom_parameters():
    """
    Test that ClassificationCrew initializes with custom parameters.
    """
    # Arrange
    # Act
    crew = ClassificationCrew(guardrail_max_retries=10, verbose=True)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == 10
    assert crew._verbose is True


def test_init_with_negative_retries():
    """
    Test that ClassificationCrew accepts negative guardrail_max_retries values.
    """
    # Arrange
    # Act
    crew = ClassificationCrew(guardrail_max_retries=-1)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == -1
    assert crew._verbose is False


def test_init_with_zero_retries():
    """
    Test that ClassificationCrew accepts zero guardrail_max_retries values.
    """
    # Arrange
    # Act
    crew = ClassificationCrew(guardrail_max_retries=0)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == 0
    assert crew._verbose is False


def test_parser_agent_with_missing_config():
    """
    Test that parser_agent handles missing parser_agent config.
    """
    # Arrange
    crew = ClassificationCrew()
    crew.agents_config = {}  # Empty config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.parser_agent()


def test_parse_task_with_missing_tasks_config():
    """
    Test that parse_task handles missing tasks_config gracefully.
    """
    # Arrange
    crew = ClassificationCrew()
    crew.agents_config = {"parser_agent": {"name": "Parser Agent"}}
    crew.tasks_config = {}  # Empty tasks_config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.parse_task()


def test_crew_with_missing_config():
    """
    Test that crew handles missing configuration gracefully.
    """
    # Arrange
    crew = ClassificationCrew()
    crew.agents_config = {}
    crew.tasks_config = {}

    # Act & Assert
    with pytest.raises(KeyError):
        crew.crew()
