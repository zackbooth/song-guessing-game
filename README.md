# Song Guessing Game
A web-based game where players guess the song title based on generated images using OpenAI's DALL·E API.

LINK: http://guessthatsong.link

## Features
- Random song selection from a DynamoDB database
- Image generation using DALL·E 3 based on song title, artist, and lyrics
- Progressive hints (release year, artist name)
- Player score tracking (wins/losses)
- Responsive design

## Tech Stack
- HTML, CSS, JavaScript, Python
- OpenAI DALL·E 3
- LocalStorage (for tracking wins/losses)

## AWS Integrations
- Lambda
- DynamoDB
- S3
- API Gateway 
- Cloudshell

## Current Progress
- [x] Song selection and image generation
- [x] Progressive hint system
- [x] Win/loss tracking using localStorage
- [ ] Optimize image generation (caching and parallel generation)
- [ ] Improve UI/UX for smoother gameplay

## Future Plans
- Add user authentication and backend for global score tracking
- Give player the option to begin the game by choosing the decade of the song's release 
- Improve image quality and optimize loading times

## Visualizations
Diagrams and flowcharts created using Excalidraw.
![song_guessing_game_FC_240917](https://github.com/user-attachments/assets/b1b14702-8437-43af-b5ec-ae0da9719ab1)


---
