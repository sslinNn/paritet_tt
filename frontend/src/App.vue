<template>
  <div class="app-container">
    <AddCardForm @card-created="handleCardCreated" />
    
    <div class="card-grid">
      <ImageCardItem v-for="answer in answers" :key="answer.id">
        <template #id>
          {{ answer.id }}
        </template>

        <template #image>
          <img :src="answer.image_data" alt="image" />
        </template>

        <template #description>
          <p>{{ answer.description }}</p>
        </template>

        <template #actions>
          <button class="delete-button" @click="handleDelete(answer.id)">
            Удалить
          </button>
        </template>
      </ImageCardItem>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { deleteCard, fetchAnswers } from '@/services/imageService'
import ImageCardItem from '@/components/ImageCardItem.vue'
import AddCardForm from '@/components/AddCardForm.vue'

const answers = ref([])

const loadAnswers = async () => {
  try {
    answers.value = await fetchAnswers()
  } catch (error) {
    console.error('Ошибка при загрузке:', error)
  }
}

onMounted(loadAnswers)

const handleDelete = async (id) => {
  try {
    await deleteCard(id)
    answers.value = answers.value.filter(answer => answer.id !== id)
  } catch (error) {
    console.error('Ошибка при удалении:', error)
  }
}

const handleCardCreated = () => {
  loadAnswers()
}
</script>

<style scoped>
.app-container {
  max-width: 1200px;
  margin: 0 auto;
  padding: 2rem;
}

.card-grid {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(300px, 1fr));
  gap: 2rem;
  margin-top: 2rem;
}

.card-image img {
  max-width: 100%;
  height: auto;
  border-radius: 6px;
  margin-bottom: 0.75rem;
}

.delete-button {
  padding: 6px 12px;
  background-color: #e74c3c;
  color: white;
  border: none;
  border-radius: 4px;
  cursor: pointer;
  transition: background-color 0.2s ease;
}

.delete-button:hover {
  background-color: #c0392b;
}
</style>

