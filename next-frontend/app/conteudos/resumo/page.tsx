import Carrossel from "@/components/ContentCarousel";
import Resumo from "@/components/ContentSummary";
import Header from "@/components/Header";
import CardRelatedContent from "@/components/CardRelatedContent";

const IMAGENS_TESTE = [
  {
    id: 1,
    url: "https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?w=800&h=450&fit=crop",
    alt: "Banner 1 - Arte Abstrata",
  },
  {
    id: 2,
    url: "https://images.unsplash.com/photo-1579546929518-9e396f3cc809?w=800&h=450&fit=crop",
    alt: "Banner 3 - Neon",
  },
  {
    id: 3,
    url: "https://images.unsplash.com/photo-1550684848-fac1c5b4e853?w=800&h=450&fit=crop",
    alt: "Banner 3 - Neon",
  },
];

const dadosResumo = {
  id: 1,
  titulo: "Matemática Básica",
  conteudo:
    "Lorem ipsum dolor sit, amet consectetur adipisicing elit. Totam nulla et in saepe! Mollitia voluptatum accusantium at non corrupti ratione, quas suscipit enim reprehenderit iusto vel ipsa officiis iure libero?",

  relacionados: [
    {
      id: 2,
      titulo: "Álgebra Linear",
    },
    {
      id: 3,
      titulo: "Geometria",
    },
    {
      id: 4,
      titulo: "Conteúdo",
    },
  ],
};

export default function conteudos() {
  return (
    <div>
      <Header />

      <main className="p-5 mt-5 sm:mt-12 mx-5">
        <Resumo dados={dadosResumo} />

        <div className="w-full mt-8 flex flex-col lg:flex-row gap-6 lg:items-start">

          <div className="w-full lg:w-2/3 lg:mt-6 min-w-0">
            <Carrossel slides={IMAGENS_TESTE} />
          </div>

          <div className="w-full lg:w-1/3 lg:mt-6 min-w-0">
            <CardRelatedContent conteudo={dadosResumo} />
          </div>

        </div>
      </main>
    </div>
  );
}