<script setup>
import { NResult } from 'naive-ui'
</script>

<template>
    <n-result
      status="403"
      title="403 Forbidden"
      description="There are always doors that are closed to you."
    >
      <template #footer>
        <n-button>Relax</n-button>
      </template>
    </n-result>
</template>