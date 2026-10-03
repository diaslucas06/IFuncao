"use client";

import { useState, useEffect, useRef } from "react";
import { Document, Page, pdfjs } from "react-pdf";

import "react-pdf/dist/Page/AnnotationLayer.css";
import "react-pdf/dist/Page/TextLayer.css";

pdfjs.GlobalWorkerOptions.workerSrc = `//unpkg.com/pdfjs-dist@${pdfjs.version}/build/pdf.worker.min.mjs`;

interface PdfSlideViewerProps {
  pdfUrl: string;
}

export default function PdfSlideViewer({ pdfUrl }: PdfSlideViewerProps) {
  const [numPages, setNumPages] = useState<number | null>(null);
  const [pageNumber, setPageNumber] = useState<number>(1);
  const [containerWidth, setContainerWidth] = useState<number>(0);

  // Referência para medir o tamanho do container pai
  const containerRef = useRef<HTMLDivElement>(null);

  // Ajusta a largura da página do PDF dinamicamente com base no tamanho do container
  useEffect(() => {
    function updateWidth() {
      if (containerRef.current) {
        // Pega a largura do container e desconta o padding interno
        setContainerWidth(containerRef.current.clientWidth - 32);
      }
    }

    updateWidth();
    window.addEventListener("resize", updateWidth);
    return () => window.removeEventListener("resize", updateWidth);
  }, []);

  function onDocumentLoadSuccess({ numPages }: { numPages: number }) {
    setNumPages(numPages);
    setPageNumber(1);
  }

  const nextPage = () => {
    if (numPages && pageNumber < numPages) {
      setPageNumber((prev) => prev + 1);
    }
  };

  const prevPage = () => {
    if (pageNumber > 1) {
      setPageNumber((prev) => prev - 1);
    }
  };

  return (
    <div className="flex flex-col items-center w-full bg-(--settings-card-color) border-(--question-card-border) rounded-md p-4 shadow-xl">
      
      <div 
        ref={containerRef}
        className="w-full flex justify-center items-center min-h-[250px] sm:min-h-[400px] rounded-xl overflow-hidden p-2"
      >
        <Document
          file={pdfUrl}
          onLoadSuccess={onDocumentLoadSuccess}
          loading={
            <div className="text-slate-400 animate-pulse font-medium py-12">
              Carregando slide...
            </div>
          }
          error={
            <div className="text-red-500 text-sm text-center py-12">
              Não foi possível carregar o PDF.
            </div>
          }
        >
          {containerWidth > 0 && (
            <Page
              pageNumber={pageNumber}
              renderTextLayer={false}
              renderAnnotationLayer={false}
              width={containerWidth} // Adapta automaticamente ao espaço disponível
              className="shadow-md rounded overflow-hidden"
            />
          )}
        </Document>
      </div>

      <div className="flex items-center justify-between w-full mt-4 px-2">
        <button
          onClick={prevPage}
          disabled={pageNumber <= 1}
          className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--neutral-300) text-(--btn-prev-text) hover:bg-(--neutral-400)"
        >
          Anterior
        </button>

        <span className="text-xs sm:text-sm font-medium">
          Slide <strong className="">{pageNumber}</strong> de{" "}
          <strong className="">{numPages || "--"}</strong>
        </span>

        <button
          onClick={nextPage}
          disabled={numPages ? pageNumber >= numPages : true}
          className="px-2 sm:px-5 py-2 rounded-full font-bold md:text-xs lp:text-base uppercase bg-(--btn-next-bg) text-(--btn-next-text) hover:bg-(--primary-500)"
        >
          Próximo
        </button>
      </div>
    </div>
  );
}