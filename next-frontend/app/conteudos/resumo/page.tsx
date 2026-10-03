'use client'

import Resumo from "@/components/ContentSummary";
import Header from "@/components/Header";
import CardRelatedContent from "@/components/CardRelatedContent";
import dadosResumo from "@/data/conteudo.json";
import dynamic from "next/dynamic";

const PdfSlideViewer = dynamic(() => import("@/components/PdfSlideViewer"), {
  ssr: false, 
});

const PDF_URL_TESTE = "/slides/GM-1-ANO.pdf";

export default function Conteudos() {
  return (
    <div>
      <Header />

      <main className="p-5 mt-2 sm:mt-6 mx-5">
        <Resumo dados={dadosResumo} />

        <div className="w-full flex flex-col lg:flex-row gap-6 lg:items-start">
          
          <div className="w-full lg:w-2/3 lg:mt-4 min-w-0">
            <PdfSlideViewer pdfUrl={PDF_URL_TESTE} />
          </div>

          <div className="w-full lg:w-1/3 lg:mt-4 min-w-0">
            <CardRelatedContent conteudo={dadosResumo} />
          </div>

        </div>
      </main>
    </div>
  );
}