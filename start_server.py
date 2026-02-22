import os
from dotenv import load_dotenv
from waitress import serve
from app import myWebsite

# Load environment variables
load_dotenv()


if __name__ == '__main__':
    # Get configuration from environment
    host = os.getenv('HOST', '0.0.0.0')
    port = int(os.getenv('PORT', 8000))
    threads = int(os.getenv('THREADS', 4))
    
    print(f"========================================")
    print(f"Starting Waitress Server...")
    print(f"Host: {host}")
    print(f"Port: {port}")
    print(f"Threads: {threads}")
    print(f"========================================")
    
    # Production server using Waitress
    serve(myWebsite, host=host, port=port, threads=threads)