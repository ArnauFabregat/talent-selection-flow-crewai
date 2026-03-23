from unittest.mock import Mock, patch

from chromadb import Collection

from talentflow.db_ingestion.chroma_client import query_to_collection, reshape_chroma_results


def test_reshape_chroma_results_with_valid_data():
    """
    Test that reshape_chroma_results correctly transforms valid ChromaDB output.
    """
    # Arrange
    chroma_output = {
        "ids": [["job1", "job2"]],
        "distances": [[0.2, 0.8]],
        "metadatas": [
            [
                {
                    "title": "Software Engineer",
                    "skills": "Python, Django",
                    "industries": "Tech",
                    "experience_level": "Mid",
                    "summary": "Backend developer",
                    "country": "USA",
                },
                {
                    "title": "Data Scientist",
                    "skills": "Python, ML",
                    "industries": "Tech",
                    "experience_level": "Senior",
                    "summary": "ML specialist",
                    "country": "Canada",
                },
            ]
        ],
    }

    # Act
    result = reshape_chroma_results(chroma_output)

    # Assert
    assert result == {
        "job1": {
            "title": "Software Engineer",
            "similarity": 0.8,
            "skills": "Python, Django",
            "industries": "Tech",
            "experience_level": "Mid",
            "summary": "Backend developer",
            "country": "USA",
        },
        "job2": {
            "title": "Data Scientist",
            "similarity": 0.2,
            "skills": "Python, ML",
            "industries": "Tech",
            "experience_level": "Senior",
            "summary": "ML specialist",
            "country": "Canada",
        },
    }


def test_reshape_chroma_results_with_missing_metadata_fields():
    """
    Test that reshape_chroma_results handles missing metadata fields gracefully.
    """
    # Arrange
    chroma_output = {"ids": [["job1"]], "distances": [[0.3]], "metadatas": [[{}]]}

    # Act
    result = reshape_chroma_results(chroma_output)

    # Assert
    assert result == {
        "job1": {
            "title": "",
            "similarity": 0.7,
            "skills": "",
            "industries": "",
            "experience_level": "",
            "summary": "",
            "country": "",
        }
    }


def test_reshape_chroma_results_with_single_result():
    """
    Test that reshape_chroma_results handles single result correctly.
    """
    # Arrange
    chroma_output = {
        "ids": [["job1"]],
        "distances": [[0.1]],
        "metadatas": [
            [
                {
                    "title": "Software Engineer",
                    "skills": "Python",
                    "industries": "Tech",
                    "experience_level": "Entry",
                    "summary": "Junior developer",
                    "country": "USA",
                }
            ]
        ],
    }

    # Act
    result = reshape_chroma_results(chroma_output)

    # Assert
    assert result == {
        "job1": {
            "title": "Software Engineer",
            "similarity": 0.9,
            "skills": "Python",
            "industries": "Tech",
            "experience_level": "Entry",
            "summary": "Junior developer",
            "country": "USA",
        }
    }


def test_query_to_collection_with_fallback_search():
    """
    Test that query_to_collection performs fallback search when country filter returns no results.
    """
    # Arrange
    mock_client = Mock()
    mock_collection = Mock(spec=Collection)

    with (
        patch("talentflow.db_ingestion.chroma_client.get_client", return_value=mock_client),
        patch("talentflow.db_ingestion.chroma_client.get_collection", return_value=mock_collection),
    ):
        # First query returns no results
        mock_collection.query.side_effect = [
            {"ids": [[]], "distances": [[]], "metadatas": [[]]},  # First call (with country)
            {
                "ids": [["job1"]],
                "distances": [[0.2]],
                "metadatas": [[{"title": "Software Engineer"}]],
            },  # Second call (fallback)
        ]

        with patch("talentflow.db_ingestion.chroma_client.reshape_chroma_results", return_value={"job1": {}}):
            # Act
            result = query_to_collection(
                collection_name="test_collection",
                query_text="Python developer",
                country="Canada",
                persist_dir="/tmp/chroma",
                top_k=3,
            )

            # Assert
            # Verify collection.query was called twice
            assert mock_collection.query.call_count == 2

            # Verify first call with country filter
            mock_collection.query.assert_any_call(
                query_texts=["Python developer"], n_results=3, where={"country": "Canada"}
            )

            # Verify second call without country filter
            mock_collection.query.assert_any_call(query_texts=["Python developer"], n_results=3)

            # Verify reshape_chroma_results was called
            assert result == {"job1": {}}


def test_query_to_collection_without_country():
    """
    Test that query_to_collection performs global search when no country is provided.
    """
    # Arrange
    mock_client = Mock()
    mock_collection = Mock(spec=Collection)

    with (
        patch("talentflow.db_ingestion.chroma_client.get_client", return_value=mock_client),
        patch("talentflow.db_ingestion.chroma_client.get_collection", return_value=mock_collection),
    ):
        mock_results = {"ids": [["job1"]], "distances": [[0.2]], "metadatas": [[{"title": "Software Engineer"}]]}
        mock_collection.query.return_value = mock_results

        with patch("talentflow.db_ingestion.chroma_client.reshape_chroma_results", return_value={"job1": {}}):
            # Act
            result = query_to_collection(
                collection_name="test_collection",
                query_text="Python developer",
                country="",
                persist_dir="/tmp/chroma",
                top_k=3,
            )

            # Assert
            # Verify collection.query was called once without country filter
            mock_collection.query.assert_called_once_with(query_texts=["Python developer"], n_results=3)

            # Verify reshape_chroma_results was called
            assert result == {"job1": {}}
