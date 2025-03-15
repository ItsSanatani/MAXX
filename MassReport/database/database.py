import motor.motor_asyncio
from config import MONGO_URI, DATABASE_NAME

class Database:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
        self.db = self.client[DATABASE_NAME]
        self.sessions = self.db["sessions"]

    async def add_session(self, user_id: int, session_string: str):
        """Add or update a user's session string."""
        await self.sessions.update_one(
            {"user_id": user_id},
            {"$set": {"session_string": session_string}},
            upsert=True
        )

    async def get_session(self, user_id: int):
        """Retrieve session string for a user."""
        session = await self.sessions.find_one({"user_id": user_id})
        return session["session_string"] if session else None

    async def remove_session(self, user_id: int):
        """Remove a user's session string."""
        await self.sessions.delete_one({"user_id": user_id})

    async def list_sessions(self):
        """List all stored session user IDs."""
        return await self.sessions.distinct("user_id")
