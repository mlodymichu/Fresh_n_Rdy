interface ImportMetaEnv {
  readonly BASE_URL: string;
  // Dodaj inne zmienne środowiskowe, jeśli są używane
}

interface ImportMeta {
  readonly env: ImportMetaEnv;
}