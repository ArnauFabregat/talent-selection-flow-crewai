from talentflow.talent_selection_flow.crews.classification_crew.enums import DocumentType
from talentflow.talent_selection_flow.crews.utils import render_to_markdown


def test_render_to_markdown_with_cv_input():
    """
    Test that render_to_markdown generates correct report for CV input.
    """
    # Arrange
    process_type = DocumentType.CV
    metadata_dict = {"name": "John Doe", "skills": "Python, Django", "experience": "5 years"}
    related_docs = {"job1": {"title": "Python Developer", "company": "Tech Corp"}}
    gap_analysis_output = {
        "docs": {"job1": {"missing_must_have": ["5+ years experience"], "matched_skills": ["Python"]}}
    }
    interview_questions_output = {
        "docs": {
            "job1": {
                "matched_skill_questions": [
                    {"question": "Tell me about your Python experience", "response": "I have 5 years..."}
                ],
                "gap_probing_questions": [
                    {"question": "Do you have experience with Django?", "response": "Yes, I have..."}
                ],
            }
        }
    }

    # Act
    result = render_to_markdown(
        process_type, metadata_dict, related_docs, gap_analysis_output, interview_questions_output
    )

    # Assert
    # Verify report contains expected sections
    assert "# Recruitment Analysis Report" in result
    assert "*Date:" in result
    assert "## Candidate summary" in result
    assert "## Matched jobs summary" in result
    assert "## Gaps analysis" in result
    assert "## Interview questions" in result

    # Verify specific content
    assert "John Doe" in result
    assert "Python Developer" in result
    assert "5+ years experience" in result
    assert "Tell me about your Python experience" in result


def test_render_to_markdown_with_empty_metadata():
    """
    Test that render_to_markdown handles empty metadata gracefully.
    """
    # Arrange
    process_type = DocumentType.CV
    metadata_dict = {}
    related_docs = {"job1": {"title": "Developer", "company": "Tech Corp"}}
    gap_analysis_output = {"docs": {"job1": {"missing_must_have": [], "matched_skills": []}}}
    interview_questions_output = {"docs": {"job1": {"matched_skill_questions": [], "gap_probing_questions": []}}}

    # Act
    result = render_to_markdown(
        process_type, metadata_dict, related_docs, gap_analysis_output, interview_questions_output
    )

    # Assert
    # Verify report still generates
    assert "# Recruitment Analysis Report" in result
    assert "## Candidate summary" in result
    assert "## Matched jobs summary" in result

    # Verify empty metadata section
    assert "- **Name**:" not in result  # No metadata to display


def test_render_to_markdown_with_no_related_docs():
    """
    Test that render_to_markdown handles no related documents.
    """
    # Arrange
    process_type = DocumentType.JOB
    metadata_dict = {"title": "Developer", "skills": "Python"}
    related_docs = {}
    gap_analysis_output = {"docs": {}}
    interview_questions_output = {"docs": {}}

    # Act
    result = render_to_markdown(
        process_type, metadata_dict, related_docs, gap_analysis_output, interview_questions_output
    )

    # Assert
    # Verify report still generates
    assert "# Recruitment Analysis Report" in result
    assert "## Job summary" in result

    # Verify related docs section is empty
    assert "## Matched cvs summary" in result
    assert "No related documents found" not in result  # Function doesn't add this message
