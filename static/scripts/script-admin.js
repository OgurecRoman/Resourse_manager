let server = {
  number: 0,
  numberCore: 0,
  Ram: 0,
  Rom: 0,
  IPAdress: '',
  OperSys: '',
}; // параметры сервера

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

function getUserData() {
  // Получаем значения из полей ввода
  const nameInput = document.querySelector('[name="name"]').value; // Значение поля для логина
  const passInput = document.querySelector('[name="password"]').value; // Значение поля для пароля

  // Записываем данные в объект
  user.name = nameInput;
  user.pass = passInput;

  // Для отладки выводим объект в консоль
  console.log(user);
}

function getServerData() {
  // Получаем все поля ввода внутри формы
  const formElements = document.querySelectorAll('.form__serv .input');

  // Перебираем поля и записываем данные в объект
  formElements.forEach((input) => {
    const name = input.name; // Получаем имя поля
    const value = input.value; // Получаем значение поля

    // В зависимости от name присваиваем значение соответствующему свойству объекта server
    switch (name) {
      case 'server__number':
        server.number = parseInt(value); // Преобразуем в число
        break;
      case 'CPU-core':
        server.numberCore = parseInt(value); // Преобразуем в число
        break;
      case 'RAM':
        server.Ram = parseInt(value); // Преобразуем в число
        break;
      case 'ROM':
        server.Rom = parseInt(value); // Преобразуем в число
        break;
      case 'IP':
        server.IPAdress = value; // Оставляем как строку
        break;
      case 'OS':
        server.OperSys = value; // Оставляем как строку
        break;
    }
  });

  // Создаём новый блок с данными
  createServerBlock();
}

// Функция для создания нового блока с сервером
function createServerBlock() {
  // Находим все теги <div> в документе
  const allDivs = document.querySelectorAll('div');

  // Проверяем, есть ли хотя бы один <div>
  if (allDivs.length > 0) {
    const lastDiv = allDivs[allDivs.length -1]; // Получаем последний <div> в документе

    // Создаём новый блок
    const newBlock = document.createElement('div');
    newBlock.classList.add('block');
    newBlock.innerHTML = `
      <h3 class="computer-number">Server Number: ${server.number}</h3>
      <p>Number of CPU: ${server.numberCore}</p>
      <p>RAM Capacity: ${server.Ram}Gb</p>
      <p>ROM: SSD ${server.Rom}Gb</p>
      <p>IP Address: ${server.IPAdress}</p>
      <p>OS: ${server.OperSys}</p>
      <div class="book__button">Забронировать</div>
    `;

    // Вставляем блок перед последним <div>
    lastDiv.parentNode.insertBefore(newBlock, lastDiv);
  } else {
    console.error('Нет тегов <div> в документе.');
  }

  // Очищаем поля формы после создания блока
  clearForm();
}






// Функция для очистки полей формы
function clearForm() {
  const formElements = document.querySelectorAll('.form__serv .input');
  formElements.forEach((input) => {
    input.value = '';
  });
}

// Обработчик для кнопки добавления сервера
document.querySelector('.submit__button-serv').addEventListener('click', (event) => {
  event.preventDefault(); // Останавливаем стандартное поведение формы
  getServerData(); // Собираем данные и создаём блок
});
  // Для отладки выводим объект в консоль
  console.log(server);


  document.getElementById('addUserButton').addEventListener('click', addUser);

  function addUser() {
    const userNameInput = document.getElementById('userNameInput');
    const userName = userNameInput.value.trim();

    if (userName === '') {
      alert('Пожалуйста, введите имя пользователя.');
      return;
    }

    // Создаем элемент списка с именем пользователя
    const li = document.createElement('li');
    li.innerHTML = `${userName} <button class="delete-button">Удалить</button>`;

    // Добавляем обработчик для кнопки удаления
    li.querySelector('.delete-button').addEventListener('click', function() {
      li.remove();
    });

    // Добавляем элемент в список
    document.querySelector('.user-list').appendChild(li);

    // Очищаем поле ввода
    userNameInput.value = '';
  }
