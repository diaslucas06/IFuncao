"use client";

import { useState, useEffect, useRef } from "react";
import { Document, Page, pdfjs } from "react-pdf";

import "react-pdf/dist/Page/AnnotationLayer.css";
import "react-pdf/dist/Page/TextLayer.css";

pdfjs.GlobalWorkerOptions.workerSrc = `https://unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;

interface PropsVisualizador {
  pdfUrl: string;
  onFinalizar?: () => void;
  finalizando?: boolean;
  finalizado?: boolean;
}

export default function PdfSlideViewer({ pdfUrl, onFinalizar, finalizando = false, finalizado = false }: PropsVisualizador) {
  const chaveStorage = `slide_atual_${pdfUrl}`;

  const [totalPaginas, setTotalPaginas] = useState<number>(0);
  const [paginaAtual, setPaginaAtual] = useState<number>(() => {
    if (typeof window !== "undefined") return Number(sessionStorage.getItem(chaveStorage)) || 1;
    return 1;
  });
  const [larguraCaixa, setLarguraCaixa] = useState<number>(600);

  const caixaRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    function atualizarLargura() {
      if (caixaRef.current) {
        const largura = caixaRef.current.clientWidth - 32;
        if (largura > 0) setLarguraCaixa(largura);
      }
    }
    atualizarLargura();
    window.addEventListener("resize", atualizarLargura);
    return () => window.removeEventListener("resize", atualizarLargura);
  }, []);

  const mudarPagina = (novaPagina: number) => {
    setPaginaAtual(novaPagina);
    sessionStorage.setItem(chaveStorage, String(novaPagina));
  };

  if (finalizado) {
    return (
      <div className="flex flex-col items-center justify-center text-center w-full min-h-[300px] sm:min-h-[450px] bg-(--settings-card-color) border border-(--question-card-border) text-(--base-text-color) rounded-md p-8 shadow-xl gap-4">
        <div className="w-16 h-16 rounded-full bg-(--btn-next-bg) text-(--btn-next-text) flex items-center justify-center text-3xl font-bold">✓</div>
        <h2 className="text-2xl sm:text-3xl font-bold">Conteúdo finalizado!</h2>
        <p className="text-sm sm:text-base opacity-80">Seu progresso foi salvo. Redirecionando para a lista de conteúdos...</p>
      </div>
    );
  }

  const ehUltimoSlide = totalPaginas > 0 && paginaAtual === totalPaginas;

  return (
    <div className="flex flex-col items-center w-full bg-(--settings-card-color) border border-(--question-card-border) text-(--base-text-color) rounded-md p-4 shadow-xl">
      <div ref={caixaRef} className="w-full flex justify-center items-center min-h-[250px] sm:min-h-[400px] rounded-xl overflow-hidden p-2">
        <Document
          file={pdfUrl}
          onLoadSuccess={({ numPages }) => setTotalPaginas(numPages)}
          loading={<div className="text-(--search-color) animate-pulse font-medium py-12">Carregando slide...</div>}
          error={<div className="text-(--error) text-sm text-center py-12">Não foi possível carregar o PDF.</div>}
        >
          <Page pageNumber={paginaAtual} renderTextLayer={false} renderAnnotationLayer={false} width={larguraCaixa} className="shadow-md rounded overflow-hidden" />
        </Document>
      </div>

      <div className="flex items-center justify-between w-full mt-4 px-2">
        <button type="button" onClick={() => mudarPagina(paginaAtual - 1)} disabled={paginaAtual <= 1} className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-prev-bg) text-(--btn-prev-text) hover:bg-(--neutral-300) dark:hover:bg-(--neutral-600) transition-colors cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed">
          Anterior
        </button>

        <span className="text-xs sm:text-sm font-medium text-(--base-text-color)">
          Slide <strong>{paginaAtual}</strong> de <strong>{totalPaginas || "--"}</strong>
        </span>

        {ehUltimoSlide ? (
          <button type="button" onClick={onFinalizar} disabled={finalizando} className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-next-bg) text-(--btn-next-text) hover:bg-(--primary-600) transition-colors cursor-pointer disabled:opacity-60 disabled:cursor-not-allowed">
            {finalizando ? "Salvando..." : "Finalizar"}
          </button>
        ) : (
          <button type="button" onClick={() => mudarPagina(paginaAtual + 1)} disabled={totalPaginas === 0} className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-next-bg) text-(--btn-next-text) hover:bg-(--primary-800) transition-colors cursor-pointer disabled:opacity-50 disabled:cursor-not-allowed">
            Próximo
          </button>
        )}
      </div>
    </div>
  );
}