<script setup lang="ts">
import type { SidebarProps } from '@/components/ui/sidebar'

import NavMain from '@/components/NavMain.vue'
import NavProjects from '@/components/NavProjects.vue'
import NavUser from '@/components/NavUser.vue'
import TeamSwitcher from '@/components/TeamSwitcher.vue'
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarRail,
} from '@/components/ui/sidebar'

import {
  AudioWaveform,
  BookOpen,
  Bot,
  Command,
  Frame,
  GalleryVerticalEnd,
  Map,
  PieChart,
  Settings2,
  SquareTerminal,
} from 'lucide-vue-next'

const props = withDefaults(defineProps<SidebarProps>(), {
  collapsible: 'icon',
})

// This is sample data.
const data = {
  user: {
    name: 'shadcn',
    email: 'm@example.com',
    avatar: '/avatars/shadcn.jpg',
  },
  teams: [
    {
      name: 'Fresh & Ready',
      logo: GalleryVerticalEnd,
      plan: 'Enterprise',
    },
  ],
  navMain: [
    {
      title: 'Dodaj łazienke',
      url: '#',
      icon: SquareTerminal,
      isActive: true,
    },
    {
      title: 'Edytuj łazienkę',
      url: '#',
      icon: Bot,
    },
    {
      title: 'Statystyki',
      url: '#',
      icon: BookOpen,
      items: [
        {
          title: 'Wykresy',
          url: '#',
        },
        {
          title: 'Dane w tabelach',
          url: '#',
        },
      ],
    },
    {
      title: 'Ustawienia',
      url: '#',
      icon: Settings2,
      items: [
        {
          title: 'Zarządzanie kadrą',
          url: '#',
        },
        {
          title: 'Zarządzanie łazienkami',
          url: '#',
        },
      ],
    },
  ],
  projects: [
    {
      name: 'Kibel 1',
      url: '#',
      icon: Frame,
    },
    {
      name: 'Kibel 2',
      url: '#',
      icon: PieChart,
    },
    {
      name: 'Kibel 3',
      url: '#',
      icon: Map,
    },
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <TeamSwitcher :teams="data.teams" />
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="data.navMain" />
      <NavProjects :projects="data.projects" />
    </SidebarContent>
    <SidebarFooter>
      <NavUser :user="data.user" />
    </SidebarFooter>
    <SidebarRail />
  </Sidebar>
</template>
