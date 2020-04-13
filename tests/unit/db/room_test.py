from unittest.mock import MagicMock, patch
import pytest

from app.models.room import Room
from app.db.room import create_room_table, write_room


@pytest.fixture
def mock_room():
    return Room.from_json({'roomId': 1, 'isOn': False, 'isVegRoom': True})


def test_write_room(mock_room):
    conn = MagicMock()

    write_room(conn, mock_room)

    conn.cursor().execute.assert_called_with("REPLACE INTO `rooms` VALUES (%s, %r, %r)", (mock_room.roomId, mock_room.isOn, mock_room.isVegRoom))

def test_create_room_table():
    conn = MagicMock()

    create_room_table(conn)
    sql = """CREATE TABLE IF NOT EXISTS rooms(
    room_id INT NOT NULL,
    is_on BOOLEAN NOT NULL,
    is_veg_room BOOLEAN NOT NULL
    );
    """

    conn.cursor().execute.assert_called_with(sql)
