<script setup lang="ts">
import NavMain from '@/components/navbar/NavMain.vue'

import NavProjects from '@/components/navbar/NavProjects.vue'
import NavSecondary from '@/components/navbar/NavSecondary.vue'
import NavUser from '@/components/navbar/NavUser.vue'
import {
  Sidebar,
  SidebarContent,
  SidebarFooter,
  SidebarHeader,
  SidebarMenu,
  SidebarMenuButton,
  SidebarMenuItem,
  type SidebarProps,
} from '@/components/ui/sidebar'
import {
  AlertCircle,
  BarChart,
  BookOpen,
  Bot, Circle,
  Command, Dot,
  Frame, HelpCircle,
  LifeBuoy,
  Map, MoreHorizontal, MoreVertical,
  PieChart, Plus,
  Send,
  Settings2, SlidersHorizontal,
  SquareTerminal, Wrench,
} from 'lucide-vue-next'

const props = withDefaults(defineProps<SidebarProps>(), {
  variant: 'inset',
})

const data = {
  user: {
    name: 'shadcn',
    email: 'm@example.com',
    avatar: '/avatars/shadcn.jpg',
  },
  navMain: [
    {
      title: 'Dodaj łazienkę',
      url: '#',
      icon: Plus,
      isActive: true,
    },
    {
      title: 'Edytuj łazienkę',
      url: '#',
      icon: SlidersHorizontal,
    },
    {
      title: 'Statystyki',
      url: '#',
      icon: BarChart,
      items: [
        {
          title: 'Wykresy',
          url: '#',
        },
        {
          title: 'Tabele',
          url: '#',
        },
      ],
    },
    {
      title: 'Ustawienia',
      url: '#',
      icon: Wrench,
      items: [
        {
          title: 'General',
          url: '#',
        },
        {
          title: 'Team',
          url: '#',
        },
        {
          title: 'Billing',
          url: '#',
        },
        {
          title: 'Limits',
          url: '#',
        },
      ],
    },
  ],
  navSecondary: [
    {
      title: 'Pomoc',
      url: '#',
      icon: HelpCircle,
    },
    {
      title: 'Kontakt',
      url: '#',
      icon: Send,
    },
  ],
  projects: [
    {
      name: 'Łazienka 1',
      url: '#',
      icon: Circle,
    },
    {
      name: 'Łazienka 2',
      url: '#',
      icon: Circle,
    },
    {
      name: 'Łazienka 3',
      url: '#',
      icon: Circle,
    },
  ],
}
</script>

<template>
  <Sidebar v-bind="props">
    <SidebarHeader>
      <SidebarMenu>
        <SidebarMenuItem>
          <SidebarMenuButton size="lg" as-child>
            <a>
              <div class="flex aspect-square size-8 items-center justify-center rounded-lg bg-sidebar-primary text-sidebar-primary-foreground">
                <Command class="size-4" />
              </div>
              <div class="grid flex-1 text-left text-sm leading-tight ">
                <span class="truncate font-semibold">Fresh & Ready</span>
                <span class="truncate text-xs"></span>
              </div>
            </a>
          </SidebarMenuButton>
        </SidebarMenuItem>
      </SidebarMenu>
    </SidebarHeader>
    <SidebarContent>
      <NavMain :items="data.navMain" />
      <NavProjects :projects="data.projects" />
      <NavSecondary :items="data.navSecondary" class="mt-auto" />
    </SidebarContent>
    <SidebarFooter>
      <NavUser :user="data.user" />
    </SidebarFooter>
  </Sidebar>
</template>