<script setup lang="ts">
import NavMain from '@/components/NavMain.vue'

import NavProjects from '@/components/NavProjects.vue'
import NavSecondary from '@/components/NavSecondary.vue'
import NavUser from '@/components/NavUser.vue'
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
  BookOpen,
  Bot,
  Command,
  Frame,
  LifeBuoy,
  Map,
  PieChart,
  Send,
  Settings2,
  SquareTerminal,
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
          title: 'Tabele',
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
      icon: LifeBuoy,
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
      icon: Frame,
    },
    {
      name: 'Łazienka 2',
      url: '#',
      icon: PieChart,
    },
    {
      name: 'Łazienka 3',
      url: '#',
      icon: Map,
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
