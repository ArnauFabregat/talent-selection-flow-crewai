from unittest.mock import patch

from talentflow.talent_selection_flow.crews.classification_crew.enums import DocumentType
from talentflow.talent_selection_flow.flow import TalentSelectionFlow


def test_handle_other_returns_warning_message():
    """
    Test that handle_other returns the correct warning message.
    """
    # Arrange
    flow = TalentSelectionFlow()

    # Act
    result = flow.handle_other()

    # Assert
    expected_message = (
        f"Invalid document type. Expected '{DocumentType.CV}' or '{DocumentType.JOB}'. Please, start a new evaluation."
    )
    assert result == expected_message


def test_handle_other_with_custom_document_types():
    """
    Test that handle_other correctly references DocumentType enum values.
    """
    # Arrange
    flow = TalentSelectionFlow()

    # Act
    result = flow.handle_other()

    # Assert
    # Verify the message contains the actual enum values
    assert DocumentType.CV in result
    assert DocumentType.JOB in result
    assert "Invalid document type" in result
    assert "Please, start a new evaluation" in result


def test_handle_other_with_verbose_logging():
    """
    Test that handle_other logs the warning message when called.
    """
    # Arrange
    flow = TalentSelectionFlow()

    # Mock logger.warning
    with patch("talentflow.talent_selection_flow.flow.logger.warning") as mock_warning:
        # Act
        flow.handle_other()

        # Assert
        # Verify logger.warning was called with the correct message
        expected_message = (
            f"Invalid document type. Expected '{DocumentType.CV}' or '{DocumentType.JOB}'. "
            "Please, start a new evaluation."
        )
        mock_warning.assert_called_once_with(expected_message)


def test_handle_other_return_value_type():
    """
    Test that handle_other returns a string value.
    """
    # Arrange
    flow = TalentSelectionFlow()

    # Act
    result = flow.handle_other()

    # Assert
    assert isinstance(result, str)
    assert len(result) > 0  # Should not return empty string
