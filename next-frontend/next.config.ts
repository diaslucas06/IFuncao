import type { NextConfig } from "next";

const nextConfig:NextConfig = {
  images: {
    remotePatterns: [
      {
        protocol: 'https',
        hostname: 'suap.ifrn.edu.br',
        port: '',
        pathname: '/djtools/arquivo/**', // Permite qualquer caminho dentro de arquivos do SUAP
      },
    ],
  },
};

export default nextConfig;
