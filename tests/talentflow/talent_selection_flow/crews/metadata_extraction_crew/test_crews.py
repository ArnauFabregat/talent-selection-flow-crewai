import pytest

from talentflow.talent_selection_flow.crews.metadata_extraction_crew.crews import (
    CVMetadataExtractorCrew,
    JobMetadataExtractorCrew,
)


def test_init_with_custom_parameters():
    """
    Test that CVMetadataExtractorCrew initializes with custom parameters.
    """
    # Arrange
    # Act
    crew = CVMetadataExtractorCrew(guardrail_max_retries=10, human_input=True, verbose=True)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == 10
    assert crew._human_input is True
    assert crew._verbose is True


def test_metadata_extractor_agent_with_missing_config():
    """
    Test that metadata_extractor_agent handles missing config.
    """
    # Arrange
    crew = CVMetadataExtractorCrew()
    crew.agents_config = {}  # Empty config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.metadata_extractor_agent()


def test_extract_metadata_task_with_missing_tasks_config():
    """
    Test that extract_metadata_task handles missing tasks_config gracefully.
    """
    # Arrange
    crew = CVMetadataExtractorCrew()
    crew.agents_config = {"cv_metadata_extractor_agent": {"name": "CV Extractor"}}
    crew.tasks_config = {}  # Empty tasks_config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.extract_metadata_task()


def test_init_with_custom_parameters():
    """
    Test that JobMetadataExtractorCrew initializes with custom parameters.
    """
    # Arrange
    # Act
    crew = JobMetadataExtractorCrew(guardrail_max_retries=10, human_input=True, verbose=True)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == 10
    assert crew._human_input is True
    assert crew._verbose is True


def test_init_with_negative_retries():
    """
    Test that JobMetadataExtractorCrew accepts negative guardrail_max_retries values.
    """
    # Arrange
    # Act
    crew = JobMetadataExtractorCrew(guardrail_max_retries=-1)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == -1
    assert crew._human_input is False
    assert crew._verbose is False


def test_init_with_zero_retries():
    """
    Test that JobMetadataExtractorCrew accepts zero guardrail_max_retries values.
    """
    # Arrange
    # Act
    crew = JobMetadataExtractorCrew(guardrail_max_retries=0)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == 0
    assert crew._human_input is False
    assert crew._verbose is False


def test_metadata_extractor_agent_with_missing_config():
    """
    Test that metadata_extractor_agent handles missing config.
    """
    # Arrange
    crew = JobMetadataExtractorCrew()
    crew.agents_config = {}  # Empty config

    # Act & Assert
    with pytest.raises(KeyError):
        crew.metadata_extractor_agent()


def test_init_with_custom_parameters():
    """
    Test that CVMetadataExtractorCrew initializes with custom parameters.
    """
    # Arrange
    # Act
    crew = CVMetadataExtractorCrew(guardrail_max_retries=10, human_input=True, verbose=True)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == 10
    assert crew._human_input is True
    assert crew._verbose is True


def test_init_with_negative_retries():
    """
    Test that CVMetadataExtractorCrew accepts negative guardrail_max_retries values.
    """
    # Arrange
    # Act
    crew = CVMetadataExtractorCrew(guardrail_max_retries=-1)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == -1
    assert crew._human_input is False
    assert crew._verbose is False


def test_init_with_zero_retries():
    """
    Test that CVMetadataExtractorCrew accepts zero guardrail_max_retries values.
    """
    # Arrange
    # Act
    crew = CVMetadataExtractorCrew(guardrail_max_retries=0)

    # Assert
    # Verify attributes are set correctly
    assert crew._guardrail_max_retries == 0
    assert crew._human_input is False
    assert crew._verbose is False
