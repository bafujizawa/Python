function gitUser(username)
{
	fetch(`https://api.github.com/users/${username}`)
	.then(response => response.json())
	.then(response => {
		element = document.getElementById('gitUserInfo')
		info = document.createTextNode(response.name + ' has ' + response.followers + ' followers')
		element.appendChild(info)
		photo = document.createElement('IMG')
		photo.src = response.avatar_url
		element.appendChild(photo)
	})
	.catch(err => console.log(err))  
}

gitUserInput = document.querySelector('#gitUserInfo')

gitUserInput.addEventListener('click', function(event){
	event.preventDefault()
	gitUser(this.children[1].value)
	
})