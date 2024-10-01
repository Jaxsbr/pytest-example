import pytest
from app.handlers.item_handler import get_items_handler, create_item_handler

@pytest.fixture
def sample_items():
    """Fixture to provide sample items data."""
    return [
        {"id": 1, "name": "Item 1"},
        {"id": 2, "name": "Item 2"}
    ]

class TestItemHandlers:
    """Test class to group item handler tests."""

    def test_get_items_handler(self, mocker, sample_items):
        """
        Test get_items_handler by mocking the fetch_items function.

        This test verifies:
        1. fetch_items is called exactly once.
        2. The returned value from get_items_handler matches the mocked result.
        """
        mock_fetch_items = mocker.patch('app.handlers.item_handler.fetch_items', return_value=sample_items)

        # Act: Call the handler
        result = get_items_handler()

        # Assert: Ensure fetch_items is called and result matches the mock data
        mock_fetch_items.assert_called_once()
        assert result == sample_items


    def test_get_items_handler_empty(self, mocker):
        """
        Test get_items_handler when no items are available.

        This ensures the handler returns an empty list when there are no items.
        """
        mock_fetch_items = mocker.patch('app.handlers.item_handler.fetch_items', return_value=[])

        # Act: Call the handler
        result = get_items_handler()

        # Assert: Ensure fetch_items is called and result is an empty list
        mock_fetch_items.assert_called_once()
        assert result == []


    def test_create_item_handler(self, mocker):
        """
        Test create_item_handler by mocking the store_item function.

        This test verifies:
        1. store_item is called exactly once with the correct input.
        2. The returned value matches the mocked store_item result.
        """
        input_argument = {"name": "Item 3"}
        expected_created_item = {"id": 3, "name": input_argument["name"]}

        mock_store_item = mocker.patch('app.handlers.item_handler.store_item', return_value=expected_created_item)

        # Act: Call the handler
        result = create_item_handler(input_argument)

        # Assert: Ensure store_item is called and result matches the expected value
        mock_store_item.assert_called_once_with(input_argument)
        assert result == expected_created_item


    @pytest.mark.parametrize("invalid_input", [
        {},          # Case 1: Valid dict but missing 'name' key
        None         # Case 2: Completely undefined/null object
    ])
    def test_create_item_handler_invalid_input(self, mocker, invalid_input):
        """
        Test create_item_handler with different invalid inputs.

        This test verifies that:
        1. The handler raises a ValueError when the 'name' key is missing.
        2. The handler raises a ValueError when input is None or undefined.
        """

        # Mocking store_item even though we don't expect it to be called
        mock_store_item = mocker.patch('app.handlers.item_handler.store_item')

        # Act & Assert: Ensure the handler raises a ValueError for invalid input
        with pytest.raises(ValueError, match="Invalid input data"):
            create_item_handler(invalid_input)

        # Assert that store_item is never called due to the error
        mock_store_item.assert_not_called()
