"use client";

import {
  Carousel,
  CarouselContent,
  CarouselItem,
  CarouselNext,
  CarouselPrevious,
} from "@/components/ui/carousel";

type SlideItem = {
  id: number;
  url: string;
  alt: string;
};

type ContentCarouselProps = {
  slides: SlideItem[];
};

export default function ContentCarousel({ slides }: ContentCarouselProps) {
  return (
    <div className="flex justify-start w-full min-w-0">
      <Carousel className="relative w-full min-w-0">

        <CarouselContent>
          {slides.map((item) => (
            <CarouselItem key={item.id} className="basis-full">
              <img src={item.url} alt={item.alt} className="w-full h-auto object-contain"
              />
            </CarouselItem>
          ))}
        </CarouselContent>

        <CarouselPrevious
          className="left-4 z-10 bg-(--background-color) text-(--base-text-color) border border-(--base-text-color)/30 shadow-md hover:opacity-90"
        />

        <CarouselNext
          className="right-4 z-10 bg-(--background-color) text-(--base-text-color) border border-(--base-text-color)/30 shadow-md hover:opacity-90"
        />

      </Carousel>
    </div>
  );
}