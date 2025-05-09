import axios from 'axios';

export async function fetchAnswers() {
  try {
    const response = await axios.get('http://localhost:8000/api/images/list/')
    return response.data
  } catch (error) {
    console.error('Ошибка при получении ответа от сервера: ', error)
    throw error
  }
}

export async function createCard(cardData) {
  try {
    const response = await axios.post(
      'http://localhost:8000/api/images/upload/',
      cardData
    )
    return response.data
  } catch (error) {
    console.error('Ошибка при создании карточки:', error)
    throw error
  }
}

export async function deleteCard(id) {
  try {
    const response = await axios.delete(`http://localhost:8000/api/images/${id}/`)
    return response.data
  } catch (error) {
    console.error('Ошибка при удалении карточки: ', error)
    throw error
  }
}