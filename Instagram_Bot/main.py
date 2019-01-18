from InstagramAPI import InstagramAPI

InstagramAPI = InstagramAPI('ProcedArtGen', 'instabot')
InstagramAPI.login()

photo_path ='/Users/abhaysinghal/Desktop/Processing Pictures/upload.jpg'
caption    =  "Alright. It works"
InstagramAPI.uploadPhoto(photo_path, caption = caption)