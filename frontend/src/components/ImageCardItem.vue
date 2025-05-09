<template>
  <div class="card">
    <div class="card-header">
      <i>
        <slot name="id"></slot>
      </i>
    </div>
    <div class="card-body">
      <div class="card-image">
        <slot name="image"></slot>
      </div>
      <div class="card-description">
        <slot name="description"></slot>
      </div>
    </div>
    <slot name="actions"></slot>
  </div>
</template>

<style scoped>
.card {
  max-width: 100%;
  margin: 1rem auto;
  border-radius: 12px;
  border: 1px solid #e0e0e0;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.05);
  overflow: hidden;
  background-color: #272727;
  transition: transform 0.2s ease, box-shadow 0.2s ease;
}

.card:hover {
  transform: translateY(-4px);
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
}

.card-header {
  padding: 0.75rem 1rem;
  font-weight: bold;
  font-size: 1.1rem;
  border-bottom: 1px solid #f0f0f0;
  background-color: #272727;
}

.card-body {
  display: flex;
  flex-direction: column;
  align-items: center;
  padding: 1rem;
}

.card-image img {
  max-width: 100%;
  height: auto;
  border-radius: 6px;
  margin-bottom: 0.75rem;
}

.card-description {
  color: #555;
  font-size: 0.95rem;
  text-align: center;
}
</style>
