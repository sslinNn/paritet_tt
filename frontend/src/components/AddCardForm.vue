<template>
  <div class="add-card-form">
    <h2>Добавить новую карточку</h2>
    <form @submit.prevent="handleSubmit">
      <div class="form-group">
        <label for="image">Изображение:</label>
        <input
          type="file"
          id="image"
          accept="image/*"
          @change="handleImageChange"
          required
        />
      </div>
      
      <div class="form-group">
        <label for="description">Описание:</label>
        <textarea
          id="description"
          v-model="description"
          required
          placeholder="Введите описание карточки"
        ></textarea>
      </div>

      <button type="submit" class="submit-button" :disabled="isLoading">
        {{ isLoading ? 'Загрузка...' : 'Добавить карточку' }}
      </button>
    </form>
  </div>
</template>

<script setup>
import { ref } from 'vue'
import { createCard } from '@/services/imageService'

const description = ref('')
const imageBase64 = ref('')
const isLoading = ref(false)

const handleImageChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    const reader = new FileReader()
    reader.onload = (e) => {
      imageBase64.value = e.target.result
    }
    reader.readAsDataURL(file)
  }
}

const handleSubmit = async () => {
  if (!imageBase64.value || !description.value) return

  isLoading.value = true
  try {
    await createCard({
      image_data: imageBase64.value,
      description: description.value
    })
    
    // Очищаем форму
    description.value = ''
    imageBase64.value = ''
    document.getElementById('image').value = ''
    
    // Эмитим событие успешного создания
    emit('card-created')
  } catch (error) {
    console.error('Ошибка при создании карточки:', error)
  } finally {
    isLoading.value = false
  }
}

const emit = defineEmits(['card-created'])
</script>

<style scoped>
.add-card-form {
  max-width: 500px;
  margin: 2rem auto;
  padding: 1.5rem;
  background-color: #272727;
  border-radius: 12px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

h2 {
  margin-bottom: 1.5rem;
  color: #fff;
  text-align: center;
}

.form-group {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.5rem;
  color: #fff;
}

input[type="file"] {
  width: 100%;
  padding: 0.5rem;
  border: 1px solid #444;
  border-radius: 4px;
  background-color: #333;
  color: #fff;
}

textarea {
  width: 100%;
  min-height: 100px;
  padding: 0.75rem;
  border: 1px solid #444;
  border-radius: 4px;
  background-color: #333;
  color: #fff;
  resize: vertical;
}

.submit-button {
  width: 100%;
  padding: 0.75rem;
  background-color: #4CAF50;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  font-size: 1rem;
  transition: background-color 0.2s ease;
}

.submit-button:hover {
  background-color: #45a049;
}

.submit-button:disabled {
  background-color: #cccccc;
  cursor: not-allowed;
}
</style> 