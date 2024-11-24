let status = ''; // буду получать с бэка admin/header_user



let user = {
  name: '',
  pass: '',
  role:'', // логин и пароль
};

let newUser = {
  name:'',
  pass:'',
}

function proverkaStatusa(status){
  if (status === 'admin') {
  // Если значение status равно "admin", добавляем класс hidden
  if (!menuBlockAdmin.classList.contains('hidden')) {
    menuBlockAdmin.classList.add('hidden');
  }
} else if (status === 'user') {
  // Если значение status равно "user", удаляем класс hidden
  if (menuBlockAdmin.classList.contains('hidden')) {
    menuBlockAdmin.classList.remove('hidden');
  }
}
}





// Correctly use `getElementsByClassName`
let menuButtonList = document.getElementsByClassName('menu')[0]; // Access the first element or specify index if multiple
let menuBlockAdmin = document.getElementsByClassName('menu__block-admin');
// Select buttons and fix event listener
const menuButtons = document.getElementsByClassName('menu__button');

// Loop through all buttons (if multiple) to add event listeners
Array.from(menuButtons).forEach((menuButton) => {
  menuButton.addEventListener('click', function () {
    if (menuButtonList.classList.contains('hidden')) {
      menuButtonList.classList.remove('hidden'); // Show menu
    } else {
      menuButtonList.classList.add('hidden'); // Hide menu
    }
  });
});
