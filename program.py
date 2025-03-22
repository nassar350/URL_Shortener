import storage
import utilites
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()
storage = storage.MemoryStorage()

class URLRequest(BaseModel):
    long_url: str

@app.post("/shorten")
def shorten_url(request: URLRequest):
    """Shorten a given URL."""
    short_url = utilites.shorten_url(request.long_url)
    storage.save(short_url, request.long_url)
    return {"short_url": short_url}

@app.get("/get/{short_url}")
def get_original_url(short_url: str):
    """Retrieve the original URL from the shortened URL."""
    long_url = storage.get(short_url)
    if not long_url:
        raise HTTPException(status_code=404, detail="URL not found")
    return {"long_url": long_url}

def main():
    print("Welcome to the URL Shortener")
    while True:
        print("\nMenu:")
        print("1. Shorten a URL")
        print("2. Get original URL")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            long_url = input("Enter the URL to shorten: ")
            short_url = utilites.shorten_url(long_url)
            storage.save(short_url, long_url)
            print(f"Shortened URL: {short_url}")

        elif choice == '2':
            short_url = input("Enter the shortened URL: ")
            long_url = storage.get(short_url)
            if long_url:
                print(f"Original URL: {long_url}")
            else:
                print("URL not found.")

        elif choice == '3':
            print("Exiting...")
            storage.get_all()
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

    # Run FastAPI in a separate thread
    # Swagger UI: http://127.0.0.1:8000/docs
    # Redoc UI: http://127.0.0.1:8000/redoc

    # Start the CLI interface
    main()

