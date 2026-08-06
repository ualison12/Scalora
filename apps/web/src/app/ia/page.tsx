const cards = [
  { title: 'Chat', value: 'Assistente contextual' },
  { title: 'Agentes', value: 'Fluxos automáticos prontos' },
  { title: 'RAG', value: 'Busca baseada em documentos' },
  { title: 'Resumo', value: 'Resumo automático de textos' },
];

export default function IAPage() {
  return (
    <main className="container">
      <header className="topbar">
        <div>
          <h1>IA</h1>
          <p className="muted">Módulo de inteligência artificial com chat, agentes e automações.</p>
        </div>
        <div className="badge">IA</div>
      </header>

      <section className="grid grid-2">
        {cards.map((card) => (
          <article key={card.title} className="card">
            <strong>{card.title}</strong>
            <p className="muted" style={{ marginTop: 8 }}>{card.value}</p>
          </article>
        ))}
      </section>
    </main>
  );
}
