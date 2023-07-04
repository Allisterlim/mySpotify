
Main goal:
I guess I just want to see how much music I listen to each day and then display that on a graph over the course of one year 

# todo items 
- [x] you've set up the firebase host. And you've created a dataset. Now you need to connect your git repo to the firebase folder directory that you created 
- [x] try to deploy the firebase server again
- [x] I need to understand how firebase hosting works, read through the documentation or bingAI it. https://firebase.google.com/docs/hosting/quickstart 
- [x] do I have to configure all files to be ignored in the firebase.json file? no.
- [x] Once you've done that, you need to figure out how to deploy the react app on the firebase host. (Front end side) https://firebase.google.com/docs/hosting/test-preview-deploy 
- [x] it looks like, we'll have to abandon the python flask stuff and rewrite the code into something compatible with firebase, which is probably npm or node js or some shit. lets look at this tutorial
- [x] once last chance before we move onto js, try this tutorial https://cloud.google.com/community/tutorials/building-flask-api-with-cloud-firestore-and-deploying-to-cloud-run 
- [ ] set up a test javascript project and try to have this run on firebase. follow this tutorial; https://firebase.google.com/docs/web/setup 
- [ ] once js website is set up, convert the python functions to js and have this run on firebase. 
- [ ] set up the firestorage database by uploading your spotify data onto the website (you can import .json as collections) 
- [ ] move your calculations and report generation code onto a server where it can do it at anytime. This means to set up the server side calculations on firebase as well. this would be done using firebase cloud functions or cloud run I think
- [ ] resize the .png file your uploading so that it's a better shape 
- [ ] clean up the .txt data your uploading so it actually looks visually nice... maybe this is where you incorporate javascript.
- [ ] set up a way for people to upload their data 
- [ ] set up a way for people to connect to the live data spotify api.
- [ ] you can try live sorting algorithms 
- [ ] create a screentime app for apple, or one for your PC 
- [ ] create one for your youtube videos and for netflix
- [ ] remove your spotify_all_time_wrapped directory as it could fk up your repo. 

# done 
- [x] join all the endsong data to process all your data up till 2022 
- [x] create a virtual env 
- [x] upload this to github (have to gitignore data)
- [x] add an output folder and add this folder to gitignore.
- [x] Create a a listening time by year  
- [x] create a listening time by month and year 
- [x] display the above information on a graph 
- [x] create your flask website to display your data
- [x] first just try to get your report to be written out onto the website server (assume that the calculations and data are done and stored locally)
- [x] modify your page and create a button on the website that will generate your spotify data and report locally 
- [x] modify this button so that it also uploads the .txt file on the website once it's generated
- [x] make it upload the graph as well.

