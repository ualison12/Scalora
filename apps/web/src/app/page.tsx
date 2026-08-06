const modules = [
  { title: 'CRM', description: 'Leads, contatos e oportunidades', accent: '#6c8cff' },
  { title: 'Financeiro', description: 'Receitas, despesas e fluxo', accent: '#34d399' },
  { title: 'Estoque', description: 'Produtos, lotes e movimentações', accent: '#f59e0b' },
  { title: 'IA', description: 'Chat, agentes, RAG e automações', accent: '#8b5cf6' },
  { title: 'Plataforma', description: 'Billing, assinaturas e deploy', accent: '#fb7185' },
  { title: 'Admin', description: 'Painel, logs e observabilidade', accent: '#38bdf8' },
];

const kpis = [
  { label: 'Receita', value: 'R$ 184,2k', change: '+18.2%' },
  { label: 'Clientes', value: '1.248', change: '+8.4%' },
  { label: 'Leads', value: '342', change: '+12.1%' },
  { label: 'Conversão', value: '24.8%', change: '+3.1%' },
];

export default function HomePage() {
  return (
    <main className="container">
      <header className="topbar">
        <div>
          <h1>Scalora OS</h1>
          <p className="muted">Painel executivo com CRM, financeiro, estoque, IA e operações.</p>
        </div>
        <div className="badge">Dark Theme · Tempo Real · White Label</div>
      </header>

      <section className="grid grid-4" style={{ marginBottom: 16 }}>
        {kpis.map((item) => (
          <article key={item.label} className="card kpi">
            <div>
              <div className="label">{item.label}</div>
              <div className="value">{item.value}</div>
            </div>
            <div className="pill">{item.change}</div>
          </article>
        ))}
      </section>

      <section className="grid grid-2" style={{ marginBottom: 16 }}>
        <article className="card">
          <div className="row" style={{ marginBottom: 12 }}>
            <strong>Visão geral</strong>
            <span className="pill">Operação saudável</span>
          </div>
          <div className="chart" />
        </article>

        <article className="card">
          <div className="row" style={{ marginBottom: 12 }}>
            <strong>Módulos ativos</strong>
            <span className="pill">6 módulos</span>
          </div>
          <div className="widget-list">
            {modules.map((module) => (
              <div key={module.title} className="widget-item" style={{ borderLeft: `4px solid ${module.accent}` }}>
                <div className="row">
                  <strong>{module.title}</strong>
                  <span className="badge">ON</span>
                </div>
                <div className="muted" style={{ marginTop: 4 }}>{module.description}</div>
              </div>
            ))}
          </div>
        </article>
      </section>

      <section className="grid grid-2">
        <article className="card">
          <strong>Resumo executivo</strong>
          <p className="muted" style={{ lineHeight: 1.6 }}>
            O ambiente está preparado para operar com CRM, financeiro, estoque e IA em uma base única. O painel central suporta métricas, automações e visão administrativa para times de produto e operação.
          </p>
        </article>
        <article className="card">
          <strong>Próximos passos</strong>
          <ul className="muted" style={{ lineHeight: 1.8 }}>
            <li>Conectar APIs externas para OpenAI, Claude, Gemini e DeepSeek.</li>
            <li>Adicionar autenticação e permissões multi-tenant.</li>
            <li>Expor microsserviços de billing, backups e observabilidade.</li>
          </ul>
        </article>
      </section>
    </main>
  );
}
