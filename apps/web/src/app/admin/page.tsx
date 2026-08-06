const adminItems = [
  { title: 'Usuários', value: '12 ativos' },
  { title: 'Logs', value: '248 entradas hoje' },
  { title: 'Backups', value: 'Último backup há 2h' },
  { title: 'Deploy', value: 'Versão 1.2.3 em prod' },
];

export default function AdminPage() {
  return (
    <main className="container">
      <header className="topbar">
        <div>
          <h1>Painel Admin</h1>
          <p className="muted">Operação, segurança e observabilidade centralizada.</p>
        </div>
        <div className="badge">Admin</div>
      </header>

      <section className="grid grid-2">
        {adminItems.map((item) => (
          <article key={item.title} className="card">
            <strong>{item.title}</strong>
            <p className="muted" style={{ marginTop: 8 }}>{item.value}</p>
          </article>
        ))}
      </section>
    </main>
  );
}
