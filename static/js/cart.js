let mybutton = document.getElementById("myBtn");
    window.onscroll = function() {scrollFunction()};
    
    
function scrollFunction() {
      if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
        mybutton.style.display = "block";
      } else {
        mybutton.style.display = "none";
      }
    }

function topFunction() {
      document.body.scrollTop = 0; 
      document.documentElement.scrollTop = 0;
 }

var updateBtns = document.getElementsByClassName('update-cart')

for(var i=0; i< updateBtns.length; i++){
    updateBtns[i].addEventListener('click',function(){
        var iId= this.dataset.product
        var action = this.dataset.action
        // console.log(iId, action, user)
        if(user === 'AnonymousUser'){
          console.log('not logged in')
        }else{
          console.log(action, typeof(action))
          updateUserOrder(iId, action)
        }
    })
}

function updateUserOrder(iID, action){
  var url = '/update_item/'
  // console.log(iID, action, user)
  fetch(url, {
    method: 'POST',
    headers:{
      'Content-Type':'application/json',
      'X-CSRFToken': csrftoken,
    },
    body:JSON.stringify({'iID': iID, 'action':action})
  })

  .then((response) =>{
    return response.json()
  })

  .then((data) =>{
    console.log(data)
    location.reload()
  })
}