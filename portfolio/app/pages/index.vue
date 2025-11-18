<template>
  <div class="max-w-6xl mx-auto py-16 px-2">
    <!-- Navbar -->

    <!-- Hero -->
    <Hero />

    <!-- About & Experience -->
    <section class="grid md:grid-cols-3 gap-8 mb-16">
      <div class="md:col-span-2">
        <h2 class="text-2xl font-semibold mb-4">About Me</h2>
        <p class="text-lg opacity-80">I started as a Python enthusiast and quickly found the perfect pairing: <strong>DRF + Nuxt</strong>. Over the past few years I built clones, production features, and end-to-end systems — most notably an AliExpress-style storefront featuring cart flows, payments integration, and scalable product APIs. I focus on pragmatic engineering: clear APIs, clean frontend components, and fast deploys.</p>

        <h3 class="mt-6 text-xl font-semibold">Latest Articles</h3>
        <div class="space-y-4 mt-4">
          <div v-for="post in posts" :key="post.slug" class="p-4 border rounded-lg">
            <div class="flex justify-between items-start">
              <div>
                <h4 class="font-semibold">{{ post.title }}</h4>
                <p class="text-sm opacity-70">{{ post.date }} • {{ post.tag }}</p>
              </div>
              <NuxtLink :to="`/blog/${post.slug}`" class="underline text-sm">Read</NuxtLink>
            </div>
            <p class="mt-2 text-sm opacity-80">{{ post.summary }}</p>
          </div>
        </div>
      </div>

      <aside>
        <h3 class="text-xl font-semibold mb-4">Experience</h3>
        <ol class="space-y-4 text-sm">
          <li>
            <strong>2023 - Present</strong>
            <div>Brand &amp; Frontend Features — Nuxt</div>
          </li>
          <li>
            <strong>2022 - 2023</strong>
            <div>Assets &amp; UI — Raycast</div>
          </li>
          <li>
            <strong>2020 - 2021</strong>
            <div>Senior UX Engineer — Linear</div>
          </li>
        </ol>

        <h3 class="mt-6 text-xl font-semibold">Skills</h3>
        <div class="mt-3 flex flex-wrap gap-2">
          <UBadge v-for="s in skills" :key="s">{{ s }}</UBadge>
        </div>
      </aside>
    </section>

    <!-- Timeline Blog (Option C style) -->
    <section class="mb-16">
      <h2 class="text-2xl font-semibold mb-6">Blog Timeline</h2>
      <div class="relative border-l pl-6">
        <div v-for="post in posts" :key="post.slug" class="mb-8 relative">
          <span class="absolute -left-3 top-2 w-3 h-3 bg-primary-600 rounded-full"></span>
          <NuxtLink :to="`/blog/${post.slug}`" class="text-lg font-semibold hover:text-primary-600">{{ post.title }}</NuxtLink>
          <div class="text-sm opacity-70">{{ post.date }} • {{ post.tag }}</div>
          <p class="mt-2 text-sm">{{ post.summary }}</p>
        </div>
      </div>
    </section>

    <!-- Testimonials -->
    <section class="mb-16">
      <h2 class="text-2xl font-semibold mb-6">Testimonials</h2>
      <div class="grid md:grid-cols-3 gap-6">
        <div v-for="t in testimonials" :key="t.name" class="p-4 border rounded-lg">
          <p class="italic">"{{ t.quote }}"</p>
          <div class="mt-4 text-sm font-semibold">{{ t.name }}</div>
          <div class="text-sm opacity-70">{{ t.role }}</div>
        </div>
      </div>
    </section>

    <!-- FAQ -->
    <section class="mb-16">
      <h2 class="text-2xl font-semibold mb-6">Frequently Asked Questions</h2>
      <UAccordion :items="faqItems" />
    </section>

  </div>
</template>

<script setup>
import Hero from '../components/Hero.vue'

const projects = Array.from({ length: 12 }).map((_, i) => ({ id: i + 1, title: `Project ${i + 1}` }))
const images = [
  "/projects/img1.png",
  "/projects/img2.png",
  "/projects/img3.png",
  "/projects/img4.png",
  "/projects/img5.png",
  "/projects/img6.png",
  "/projects/img7.png",
  "/projects/img8.png",
  "/projects/img9.png",
  "/projects/img10.png",
  "/projects/img11.png",
  "/projects/img12.png",
  "/projects/img13.png",
]

const posts = [
  { slug: 'from-mockup-to-market', title: 'From Mockup to Market: My End-to-End Product Design Process', date: 'Apr 23, 2025', tag: 'Product', summary: 'A detailed breakdown of iterative design methodology.' },
  { slug: 'psychology-of-color', title: 'The Psychology of Color in UI Design', date: 'Mar 15, 2025', tag: 'Design', summary: 'How strategic color choices influence behaviour.' },
  { slug: 'design-system', title: 'How I Built My Design System from Scratch', date: 'Mar 5, 2025', tag: 'System', summary: 'A practical guide to creating a design system.' }
]

const testimonials = [
  { name: 'Sarah Chen', role: 'Product Director at Bloom Finance', quote: "Emma's approach to UX design completely transformed our product. It reduced support tickets by 40%." },
  { name: 'Michael Rodriguez', role: 'Co-founder of Wavelength Music', quote: "Working with Emma was the best decision we made for our startup." },
  { name: 'Dr. Aisha Johnson', role: 'Chief Innovation Officer at GreenTech Solutions', quote: "Emma stands out in her ability to translate complex data into intuitive interfaces." }
]

const skills = ['Python', 'Django', 'DRF', 'Nuxt', 'Vue', 'My-SQL', 'Tailwind', 'Docker']

const faqItems = [
  { label: 'What services do you offer?', content: 'I build end-to-end web applications, including APIs, frontend, and deployment.' },
  { label: 'What is your development process like?', content: 'Research → Prototype → Build → Test → Deploy. I prefer small iterative releases.' },
  { label: 'Do you work with startups?', content: 'Yes — I love working with early-stage teams to build product-market fit.' }
]
</script>
<style lang="css" scoped>
@refrence '~/assets/css/main.css';
</style>