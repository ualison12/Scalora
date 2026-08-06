const modules = [
  { title: 'CRM', summary: 'Gestão de contatos, leads e oportunidades.' },
  { title: 'Financeiro', summary: 'Fluxo de caixa, contas e recebimentos.' },
  { title: 'Estoque', summary: 'Produtos, lotes, validade e movimentos.' },
  { title: 'IA', summary: 'Chat, agentes, automações e RAG.' },
  { title: 'Plataforma', summary: 'Billing, assinaturas, webhooks e deploy.' },
  { title: 'Admin', summary: 'Logs, backups e observabilidade.' },
];

export default function ModulesPage() {
  return (
    <main className="container">
      <header className="topbar">
        <div>
          <h1>Módulos</h1>
          <p className="muted">Visão consolidada dos principais blocos da plataforma.</p>
        </div>
        <div className="badge">Multi módulo</div>
      </header>

      <section className="grid grid-2">
        {modules.map((module) => (
          <article key={module.title} className="card">
            <div className="row" style={{ marginBottom: 8 }}>
              <strong>{module.title}</strong>
              <span className="pill">Ativo</span>
            </div>
            <p className="muted" style={{ margin: 0 }}>{module.summary}</p>
          </article>
        ))}
      </section>
    </main>
  );
}
