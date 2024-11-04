# Image Playlist Generator

**Purpose of the tool** 

The Image Playlist Generator tool aims to create music playlists based on  user-uploaded images. By analysing the content of the photos, the tool will curate  Spotify playlists that match the themes and activities depicted. This innovative approach has the  potential to deepen users’ connection to their music and memories.

**Features**  

- Image Upload: Users can upload images from their device or take photos  directly within the app. 
-  Automatic Playlist Generation: Based on the analysis of the uploaded image,  the app will generate a Spotify playlist that reflects the themes or activities in the  photo (e.g., a beach scene could generate a summery playlist).

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)

## Installation

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/project-name.git
```

Navigate to the project directory:

```
cd project-name
```

Create and activate a virtual environment:

```
python -m venv venv
source venv/bin/activate  # For Windows: venv\Scripts\activate
```

Install the dependencies:

```
pip install -r requirements.txt
```

## Usage

**To use the Imagga API, follow these steps:**

1. **Register for an Account**: Go to [Imagga](https://imagga.com/) and create an account. After registration, you will receive your API key and secret.

2. **Install Required Libraries**: Ensure you have the necessary libraries installed. You can do this using pip:

   ```bash
   pip install requests
   ```

3. **Set Up Your API Credentials**: Store your API key and secret in a configuration file (e.g., `Imagga_key.txt`) in the following format:

   ```bash
   {
       "api_key": "YOUR_API_KEY",
       "api_secret": "YOUR_API_SECRET"
   }
   
   ```

4. **Analyze Images**: Replace `image_url` with the URL of the image you want to analyze. Run the script to get the image tags returned from the Imagga API.

5. **Handle the API Response**: The response will contain tags associated with the image. You can modify the code to handle the response data as needed for your application.



**To use the Spotify API, follow these steps:**

1. **Create a Spotify Account**: If you don’t have a Spotify account, sign up at [Spotify](https://www.spotify.com/).

2. **Register as a Developer**: Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your account credentials.

3. **Create a New Application**: Click on "Create an App." Fill out the application details, including the app name and description. After creating the app, you will receive your **Client ID** and **Client Secret**.

4. **Set Up Redirect URI**: In your app settings, add a **Redirect URI** (e.g., `http://localhost:8888/callback`). This URI will be used for authentication.

5. **Install Required Libraries**: Ensure you have the `spotipy` library installed. You can do this using pip:

   ```
   pip install spotipy
   ```

6. **Authenticate Your Application**: Use the following code snippet to authenticate with your **Client ID** and **Client Secret**:

   ```
   import spotipy
   from spotipy.oauth2 import SpotifyOAuth
   
   sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id='YOUR_CLIENT_ID',
                                                  client_secret='YOUR_CLIENT_SECRET',
                                                  redirect_uri='YOUR_REDIRECT_URI',
                                                  scope='user-library-read'))
   
   ```



## Examples

***Input image***

![](https://i.pinimg.com/564x/96/78/c4/9678c4bc9f52e15b777c622a79610d1f.jpg)



***Play list***

<img src="C:\Users\Qianlan\Desktop\Spotify Premium 04_11_2024 17_16_45.PNG" alt="Spotify Premium 04_11_2024 17_16_45" style="zoom: 50%;" />