"""Point d'entrée principal de NearMeet"""

import sys
import argparse
from src.core.app import NearMeetApp
from src.utils.logger import setup_logging

logger = setup_logging()


def main():
    """Main entry point"""
    parser = argparse.ArgumentParser(
        description="NearMeet - Application de communication locale"
    )
    
    parser.add_argument(
        "--mode",
        choices=["client", "server"],
        default="client",
        help="Mode de fonctionnement (client ou serveur)"
    )
    
    parser.add_argument(
        "--host",
        type=str,
        default="127.0.0.1",
        help="Adresse du serveur (mode client)"
    )
    
    parser.add_argument(
        "--port",
        type=int,
        default=5000,
        help="Port de connexion"
    )
    
    parser.add_argument(
        "--username",
        type=str,
        help="Nom d'utilisateur"
    )
    
    parser.add_argument(
        "--debug",
        action="store_true",
        help="Mode debug"
    )
    
    args = parser.parse_args()
    
    # Create and run application
    app = NearMeetApp(mode=args.mode)
    app.run()


if __name__ == "__main__":
    main()
