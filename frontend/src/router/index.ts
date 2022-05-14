import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    redirect: "/index",
  },

  {
    path: "/places/:type",
    component: () => import("../pages/LocalBusinesses.vue"),
    props: (route) => ({
      type: route.params.type,
    }),
  },
  {
    path: "/index",
    component: () => import("../pages/Index.vue"),
  },
  {
    path: "/home",
    component: () => import("../pages/Home.vue"),
  },
  {
    path: "/test",
    component: () => import("../pages/Test.vue"),
  },
  {
    path: "/recommendations",
    component: () => import("../pages/RecommendationsHF.vue"),
  },
  {
    path: "/rating",
    component: () => import("../pages/Rating.vue"),
  },
  {
    path: "/timeline",
    component: () => import("../pages/TimelineHF.vue"),
  },
  {
    path: "/route",
    component: () => import("../pages/Route.vue"),
  },
  {
    path: "/afterhome",
    component: () => import("../pages/AfterHome.vue"),
  },
  {
    path: "/afterafterhome",
    component: () => import("../pages/AfterAfterHome.vue"),
  },
  {
    path: "/end",
    component: () => import("../pages/End.vue"),
  },
  {
    path: "/break",
    component: () => import("../pages/Break.vue"),
  },
];

const router = createRouter({
  history: createWebHistory(),
  routes,
});

export default router;
