import './globals.css';
import type { Metadata } from 'next';

export const metadata: Metadata = {
  title: 'Scalora Dashboard',
  description: 'Painel executivo com KPIs, gráficos, estoque e IA',
};

export default function RootLayout({ children }: { children: React.ReactNode }) {
  return (
    <html lang="pt-BR">
      <body>{children}</body>
    </html>
  );
}
