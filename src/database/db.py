"""Database initialization and management"""

import sqlite3
from pathlib import Path
from typing import Optional
from src.config import DatabaseConfig
from src.utils.logger import get_logger

logger = get_logger(__name__)


class Database:
    """SQLite database manager"""
    
    def __init__(self, db_path: Optional[Path] = None):
        """Initialize database"""
        self.db_path = db_path or DatabaseConfig.PATH
        self.connection: Optional[sqlite3.Connection] = None
        self.init_db()
    
    def init_db(self):
        """Initialize database and create tables"""
        try:
            self.connection = sqlite3.connect(
                str(self.db_path),
                timeout=DatabaseConfig.TIMEOUT
            )
            self.connection.row_factory = sqlite3.Row
            self._create_tables()
            logger.info(f"Database initialized at {self.db_path}")
        except Exception as e:
            logger.error(f"Failed to initialize database: {e}", exc_info=True)
            raise
    
    def _create_tables(self):
        """Create database tables"""
        try:
            cursor = self.connection.cursor()
            
            # Users table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS users (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    username TEXT UNIQUE NOT NULL,
                    status TEXT DEFAULT 'offline',
                    last_seen TIMESTAMP,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    profile_picture BLOB
                )
            """)
            
            # Messages table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS messages (
                    id TEXT PRIMARY KEY,
                    sender TEXT NOT NULL,
                    content TEXT NOT NULL,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    is_encrypted BOOLEAN DEFAULT 0,
                    reply_to TEXT,
                    FOREIGN KEY (sender) REFERENCES users (username)
                )
            """)
            
            # File transfers table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS file_transfers (
                    id TEXT PRIMARY KEY,
                    sender TEXT NOT NULL,
                    recipient TEXT NOT NULL,
                    filename TEXT NOT NULL,
                    filesize INTEGER,
                    status TEXT DEFAULT 'pending',
                    checksum TEXT,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    completed_at TIMESTAMP,
                    FOREIGN KEY (sender) REFERENCES users (username),
                    FOREIGN KEY (recipient) REFERENCES users (username)
                )
            """)
            
            # Sessions table
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS sessions (
                    id TEXT PRIMARY KEY,
                    user_id TEXT NOT NULL,
                    token TEXT UNIQUE NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    expires_at TIMESTAMP,
                    ip_address TEXT,
                    is_active BOOLEAN DEFAULT 1,
                    FOREIGN KEY (user_id) REFERENCES users (username)
                )
            """)
            
            self.connection.commit()
            logger.info("Database tables created/verified")
        except Exception as e:
            logger.error(f"Failed to create tables: {e}", exc_info=True)
            raise
    
    def close(self):
        """Close database connection"""
        if self.connection:
            self.connection.close()
            logger.info("Database connection closed")
    
    def execute(self, query: str, params: tuple = ()):
        """Execute a query"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            self.connection.commit()
            return cursor
        except Exception as e:
            logger.error(f"Database error: {e}", exc_info=True)
            raise
    
    def fetch_one(self, query: str, params: tuple = ()):
        """Fetch one row"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchone()
        except Exception as e:
            logger.error(f"Database error: {e}", exc_info=True)
            raise
    
    def fetch_all(self, query: str, params: tuple = ()):
        """Fetch all rows"""
        try:
            cursor = self.connection.cursor()
            cursor.execute(query, params)
            return cursor.fetchall()
        except Exception as e:
            logger.error(f"Database error: {e}", exc_info=True)
            raise
    
    def __enter__(self):
        """Context manager entry"""
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        """Context manager exit"""
        self.close()
