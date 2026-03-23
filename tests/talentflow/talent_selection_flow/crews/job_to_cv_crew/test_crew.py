import pytest

from talentflow.talent_selection_flow.crews.job_to_cv_crew.crew import JobToCVCrew


def test_init_with_custom_parameters():
    """
    Test that JobToCVCrew initializes with custom parameters.
    """
    # Arrange
    # Act
    crew = JobToCVCrew(guardrail_max_retries=10, verbose=True)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == 10
    assert crew._verbose is True


def test_init_with_negative_retries():
    """
    Test that JobToCVCrew accepts negative guardrail_max_retries values.
    """
    # Arrange
    # Act
    crew = JobToCVCrew(guardrail_max_retries=-1)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == -1
    assert crew._verbose is False


def test_init_with_zero_retries():
    """
    Test that JobToCVCrew accepts zero guardrail_max_retries values.
    """
    # Arrange
    # Act
    crew = JobToCVCrew(guardrail_max_retries=0)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == 0
    assert crew._verbose is False


def test_gap_identifier_agent_with_missing_config():
    """
    Test that gap_identifier_agent handles missing config.
    """
    # Arrange
    crew = JobToCVCrew()
    crew.agents_config = {}  # Empty config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.gap_identifier_agent()


def test_interview_question_generator_agent_with_missing_config():
    """
    Test that interview_question_generator_agent handles missing config.
    """
    # Arrange
    crew = JobToCVCrew()
    crew.agents_config = {}  # Empty config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.interview_question_generator_agent()


def test_identify_gaps_task_with_missing_tasks_config():
    """
    Test that identify_gaps_task handles missing tasks_config gracefully.
    """
    # Arrange
    crew = JobToCVCrew()
    crew.tasks_config = {}

    # Act & Assert
    with pytest.raises(KeyError):
        crew.identify_gaps_task()


def test_generate_interview_questions_task_with_missing_tasks_config():
    """
    Test that generate_interview_questions_task handles missing tasks_config gracefully.
    """
    # Arrange
    crew = JobToCVCrew()
    crew.agents_config = {"interview_question_generator_agent": {"name": "Interview Coach"}}
    crew.tasks_config = {}  # Empty tasks_config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.generate_interview_questions_task()


def test_crew_with_missing_config():
    """
    Test that crew handles missing configuration gracefully.
    """
    # Arrange
    crew = JobToCVCrew()
    crew.agents_config = {}
    crew.tasks_config = {}

    # Act & Assert
    with pytest.raises(KeyError):
        crew.crew()
