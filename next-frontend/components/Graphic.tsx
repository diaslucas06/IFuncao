import BarraGrafico from "./BarItem"

const dados = [
  {
    nome: "Matemática Básica",
    porcentagem: 37.3,
  },
  {
    nome: "Estatística",
    porcentagem: 11.2,
  },
  {
    nome: "Geometria Espacial",
    porcentagem: 11.2,
  },
  {
    nome: "Funções",
    porcentagem: 10.2,
  },
  {
    nome: "Probabilidade",
    porcentagem: 5.2,
  },
  {
    nome: "Geometria Plana",
    porcentagem: 7.7,
  },
  {
    nome: "Análise Combinatória",
    porcentagem: 4.1,
  },
  {
    nome: "Trigonometria",
    porcentagem: 3.7,
  },
]

export default function GraficoEnem() {
  return (
    <div className="mt-6 h-full w-full rounded-xl bg-(--settings-card-color) p-4 md:p-6">

      <h2 className="text-center sm:text-left font-extrabold text-xl md:text-[28px] lg:text-[32px] pc:text-[48px]">
        Conteúdos mais recorrentes no ENEM
      </h2>

      <div className="mt-6 overflow-x-auto [scrollbar-width:none] [&::-webkit-scrollbar]:hidden">
          <div className="relative w-max pl-10">

            <div className="absolute left-0 top-0 flex h-32 w-10 flex-col justify-between text-xs text-gray-500 sm:h-40 md:h-48 lg:h-64">
              <p>40%</p>
              <p>30%</p>
              <p>20%</p>
              <p>10%</p>
              <p>0%</p>
            </div>

            <div className="pointer-events-none absolute left-10 right-0 top-0 z-0 flex h-32 flex-col justify-between sm:h-40 md:h-48 lg:h-64">
              <div className="border-t border-black/10" />
              <div className="border-t border-black/10" />
              <div className="border-t border-black/10" />
              <div className="border-t border-black/10" />
              <div className="border-t border-black/10" />
            </div>

            <div className="relative z-10 flex gap-4 lg:gap-6">
              {dados.map((item, index) => (
                <BarraGrafico key={`${item.nome}-${index}`} nome={item.nome} porcentagem={item.porcentagem}
                />
              ))}
            </div>

          </div>

        </div>
    </div>
  )
}