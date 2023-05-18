const headers = document.querySelectorAll('.subtitle');
const textBlocks = document.querySelectorAll('.text-block');

// Добавляем обработчик клика на каждый заголовок
headers.forEach((header, index) => {
  header.addEventListener('click', (e) => {
    e.preventDefault();
    // Если текстовый блок скрыт, показываем его
    if (!textBlocks[index].style.display || textBlocks[index].style.display==='none') {
      textBlocks[index].style.display = 'block';
      header.style.backgroundColor = '#ccc';
    }
    // Иначе скрываем текстовый блок
    else {
      textBlocks[index].style.display = 'none';
      header.style.backgroundColor = 'rgb(238, 235, 233)';
    }
  });
});

const images = document.querySelectorAll('.image');

images.forEach((image) => {
    image.addEventListener('mouseover', (e) => {
      e.preventDefault();
      image.style.width = '500px';
      image.style.borderRadius = '0px';
      image.style.marginLeft = "5%";
    });
});

images.forEach((image) => {
    image.addEventListener('mouseout', (e) => {
      e.preventDefault();
      image.style.width = '350px';
      image.style.borderRadius = '10px';
      image.style.marginLeft = "50px";
    });
});