import GraficoEnem from "@/components/Graphic";
import Header from "@/components/Header";
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from "@/components/ui/carousel";
import CardHistorico from "@/components/CardHistorico";
import { CardBackground } from "@/components/CardProfile";

export default function conteudos() {
   let historico = [
        {'id': 1, 'nome': 'MATEMÁTICA BÁSICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 50},
        {'id': 2, 'nome': 'TRIGONOMETRIA', 'link': '/conteudos/matematica_basica', 'porcentagem': 0},
        {'id': 3, 'nome': 'GEOMETRIA', 'link': '/conteudos/matematica_basica', 'porcentagem': 80},
        {'id': 4, 'nome': 'PROGRESSÃO ARITMÉTICA', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
        {'id': 5, 'nome': 'MATEMÁTICA FINANCEIRA', 'link': '/conteudos/matematica_basica', 'porcentagem': 40},
        {'id': 6, 'nome': 'MATRIZ', 'link': '/conteudos/matematica_basica', 'porcentagem': 100},
    ]

  return (
    <div>
      <Header />

      <section className="m-5 md:m-10">
        <h1 className="text-[24px] md:text-[40px] lg:text-[48px] lp:text-[56px] pc:text-[64px] font-bold">Enem</h1>
        <GraficoEnem/>

        <CardBackground className="w-full bg-(--settings-card-color) mt-6">
            <div className="flex flex-wrap gap-3 lg:gap-8 lp:gap-11">
                {historico.map((conteudo, index) => (
                    <div key={conteudo.id} className="basis-1/3 lg:basis-8/26 lp:basis-2/9 pc:basis-3/13">
                        <CardHistorico nome={conteudo.nome}  link={conteudo.link}  porcentagem={conteudo.porcentagem} index={index}/> 
                    </div>
                ))}
            </div>
        </CardBackground>

      </section>
    </div>
  );
}