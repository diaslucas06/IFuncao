interface BarraGraficoProps {
  nome: string
  porcentagem: number
}

export default function BarraGrafico({
  nome,
  porcentagem,
}: BarraGraficoProps) {
  return (
    <div className="flex w-full min-w-0 flex-col items-center">
    
      <div className="flex h-32 w-14 items-end sm:h-40 sm:w-16 md:h-48 md:w-20 lg:h-64 lg:w-24 pc:w-28">

        <div className="w-full rounded-sm bg-(--primary-300)"
          style={{ height: `${porcentagem * 2.5}%` }}
        />

      </div>

      <p className="font-normal text-sm md:text-xl pc:text-2xl mt-0.5">
        {porcentagem}%
      </p>

      <p className="w-full text-center text-sm font-normal leading-tight  md:text-xl pc:text-2xl">
        {nome}
      </p>

    </div>
  )
}