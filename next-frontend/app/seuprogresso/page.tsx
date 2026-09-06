import CardStatus from "@/components/CardStatus";
import Header from "@/components/Header";
import { BookOpen, CircleCheckBig, Target, Flame } from "lucide-react";
import StudySuggestion from "@/components/StudySuggestion";

export default function Progresso() {
  const dadosProgresso = {
    assuntosConcluidos: 3,
    totalAssuntos: 30,
    questoesRespondidas: 120,
    totalAcertos: 89,
    ofensiva: 10,
    conteudoRecomendado: "Análise Combinatória",
    etapa: 1,
  };

  return (
    <div className="min-h-screen flex flex-col bg-(--background-color)">
      <Header />

      <main className="flex-1 w-full mx-auto p-4 sm:p-6 lg:p-10">
        <section className="bg-(--settings-card-color) p-5 sm:p-8 rounded-xl shadow-sm border border-(--background-color)">
          
          <h1 className="text-2xl sm:text-3xl lg:text-4xl font-bold text-(--link-color)">
            Sua Evolução
          </h1>

          <div className="grid grid-cols-2 lg:grid-cols-4 gap-4 lg:gap-6 mt-6">
            
            <CardStatus
              titulo="Assuntos concluídos" valor={`${dadosProgresso.assuntosConcluidos}/${dadosProgresso.totalAssuntos}`} icone={BookOpen} bgColor="bg-(--neutral-0)"
              textColor="text-(--neutral-900)" iconeColor="text-(--primary-300)"
            />

            <CardStatus
              titulo="Questões respondidas" valor={String(dadosProgresso.questoesRespondidas)} icone={CircleCheckBig} bgColor="bg-(--primary-800)"
              textColor="text-(--neutral-0)" iconeColor="text-(--neutral-0)"
            />

            <CardStatus
              titulo="Total de acertos" valor={`${dadosProgresso.totalAcertos}%`} icone={Target} bgColor="bg-(--primary-300)"
              textColor="text-(--neutral-0)" iconeColor="text-(--neutral-0)"
            />

            <CardStatus titulo="Ofensiva" valor={String(dadosProgresso.ofensiva)} icone={Flame} bgColor="bg-(--primary-200)" textColor="text-(--neutral-0)"
              iconeColor="text-(--neutral-0)" descricao="dias"
            />

            <div className="col-span-2 mt-2">
              <StudySuggestion
                conteudoRecomendado={dadosProgresso.conteudoRecomendado}
                etapa={dadosProgresso.etapa}
              />
            </div>

          </div>
        </section>
      </main>
    </div>
  );
}